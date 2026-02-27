import cv2
import numpy as np
import time

# 初始化摄像头
cap = cv2.VideoCapture(0)

# 检查摄像头是否成功打开
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

# 获取帧的宽度和高度
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"摄像头分辨率: {frame_width}x{frame_height}")

# 创建背景减法器用于检测运动
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)

# 形态学操作的内核
kernel = np.ones((5, 5), np.uint8)

# 创建显示窗口
cv2.namedWindow('动态物体检测', cv2.WINDOW_NORMAL)
cv2.resizeWindow('动态物体检测', frame_width, frame_height)

print("动态物体检测已启动!")
print("检测画面中的运动物体并添加边框")
print("按 'q' 键退出程序")
print("按 'r' 键重置背景模型")
print("按 '+' 键增加检测灵敏度")
print("按 '-' 键减少检测灵敏度")

# 检测参数
sensitivity = 25  # 检测灵敏度（阈值）
min_area = 500  # 最小检测区域面积

# 边框颜色和样式
colors = [
    (0, 255, 0),  # 绿色
    (255, 0, 0),  # 蓝色
    (0, 0, 255),  # 红色
    (255, 255, 0),  # 青色
    (255, 0, 255),  # 紫色
    (0, 255, 255)  # 黄色
]

# 用于存储检测历史
detection_history = []
max_history = 10

# 帧率计算
fps_counter = 0
fps_start_time = time.time()

while True:
    # 读取摄像头帧
    ret, frame = cap.read()

    if not ret:
        print("无法获取帧")
        break

    # 翻转帧，使显示更像镜子
    frame = cv2.flip(frame, 1)

    # 应用背景减除
    fgmask = fgbg.apply(frame)

    # 应用阈值处理
    _, fgmask = cv2.threshold(fgmask, sensitivity, 255, cv2.THRESH_BINARY)

    # 应用形态学操作去除噪声
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.dilate(fgmask, kernel, iterations=2)

    # 查找轮廓
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 创建一份原始帧的副本用于绘制
    result_frame = frame.copy()

    # 检测到的物体计数
    detected_objects = 0

    # 处理检测到的运动区域
    for contour in contours:
        # 计算轮廓面积
        area = cv2.contourArea(contour)

        # 只处理足够大的轮廓
        if area > min_area:
            detected_objects += 1

            # 获取轮廓的边界框
            x, y, w, h = cv2.boundingRect(contour)

            # 计算边界框中心点
            center_x = x + w // 2
            center_y = y + h // 2

            # 计算运动速度（与历史位置比较）
            current_time = time.time()
            speed = 0
            for history in detection_history:
                hx, hy, hw, hh, htime = history
                if current_time - htime < 1.0:  # 只考虑1秒内的历史
                    distance = np.sqrt((center_x - hx) ** 2 + (center_y - hy) ** 2)
                    time_diff = current_time - htime
                    if time_diff > 0:
                        speed = distance / time_diff
                        break

            # 根据速度选择颜色（速度越快，颜色越暖）
            color_idx = min(5, int(speed / 10))
            color = colors[color_idx]

            # 绘制边界框
            cv2.rectangle(result_frame, (x, y), (x + w, y + h), color, 2)

            # 绘制中心点
            cv2.circle(result_frame, (center_x, center_y), 5, color, -1)

            # 显示面积信息
            cv2.putText(result_frame, f"Area: {int(area)}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

            # 显示速度信息（如果速度大于0）
            if speed > 0:
                cv2.putText(result_frame, f"Speed: {speed:.1f} px/s", (x, y - 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

            # 添加到检测历史
            detection_history.append((center_x, center_y, w, h, current_time))

            # 限制历史记录数量
            if len(detection_history) > max_history:
                detection_history.pop(0)

    # 计算并显示帧率
    fps_counter += 1
    if time.time() - fps_start_time >= 1.0:
        fps = fps_counter / (time.time() - fps_start_time)
        fps_counter = 0
        fps_start_time = time.time()

        # 显示帧率
        cv2.putText(result_frame, f"FPS: {fps:.1f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # 显示检测到的物体数量
    cv2.putText(result_frame, f"Objects: {detected_objects}", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # 显示检测参数
    cv2.putText(result_frame, f"Sensitivity: {sensitivity}", (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
    cv2.putText(result_frame, f"Min Area: {min_area}", (10, 110),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

    # 显示操作提示
    cv2.putText(result_frame, "Press 'q' to quit, 'r' to reset, '+'/'-' to adjust sensitivity",
                (10, frame_height - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

    # 显示检测掩码（小窗口）
    mask_display = cv2.resize(fgmask, (200, 150))
    mask_display_color = cv2.cvtColor(mask_display, cv2.COLOR_GRAY2BGR)
    result_frame[10:160, frame_width - 210:frame_width - 10] = mask_display_color

    # 在掩码窗口上添加标签
    cv2.putText(result_frame, "Motion Mask", (frame_width - 200, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # 显示结果
    cv2.imshow('动态物体检测', result_frame)

    # 键盘输入处理
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('r'):
        # 重置背景模型
        fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)
        detection_history = []
        print("背景模型已重置")
    elif key == ord('+') or key == ord('='):
        # 增加检测灵敏度（降低阈值）
        sensitivity = max(5, sensitivity - 5)
        print(f"检测灵敏度增加: {sensitivity}")
    elif key == ord('-') or key == ord('_'):
        # 减少检测灵敏度（提高阈值）
        sensitivity = min(100, sensitivity + 5)
        print(f"检测灵敏度减少: {sensitivity}")
    elif key == ord('a'):
        # 增加最小检测区域
        min_area = min(5000, min_area + 100)
        print(f"最小检测区域: {min_area}")
    elif key == ord('z'):
        # 减少最小检测区域
        min_area = max(100, min_area - 100)
        print(f"最小检测区域: {min_area}")

# 释放摄像头并关闭窗口
cap.release()
cv2.destroyAllWindows()
print("程序已退出")