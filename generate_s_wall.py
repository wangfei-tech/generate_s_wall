import math

def generate_s_wall(
    filename="s_arc_wall.sdf",
    radius=1.5,
    thickness=0.2,
    height=1.0,
    arc_sections=32
):
    angle_step = math.pi / arc_sections  # 半圆分段
    wall_blocks = []

    # 第一段圆弧（左弧），从 π 到 0，逆时针
    for i in range(arc_sections + 1):  # 多一个点确保闭合
        angle = math.pi - i * angle_step  # 从 π 到 0
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        yaw = angle + math.pi / 2  # 法线方向
        wall_blocks.append((x, y, yaw))

    # 第二段圆弧（右弧），从 0 到 -π，顺时针，沿 x 轴平移 2*radius
    for i in range(arc_sections + 1):
        angle = 0 - i * angle_step  # 从 0 到 -π
        x = 2 * radius + radius * math.cos(angle)
        y = radius * math.sin(angle)
        yaw = angle + math.pi / 2  # 这里也用相同的法线方向计算方式
        wall_blocks.append((x, y, yaw))

    # 生成 SDF 文件
    with open(filename, "w") as f:
        f.write('<?xml version="1.0" ?>\n')
        f.write('<sdf version="1.6">\n')
        f.write('  <model name="s_arc_wall">\n')
        f.write('    <static>true</static>\n')

        for idx, (x, y, yaw) in enumerate(wall_blocks):
            f.write(f'    <link name="wall_{idx}">\n')
            f.write(f'      <pose>{x:.3f} {y:.3f} {height/2:.3f} 0 0 {yaw:.3f}</pose>\n')
            f.write('      <collision name="collision">\n')
            f.write('        <geometry>\n')
            f.write(f'          <box><size>{thickness} {radius * angle_step:.3f} {height}</size></box>\n')
            f.write('        </geometry>\n')
            f.write('      </collision>\n')
            f.write('      <visual name="visual">\n')
            f.write('        <geometry>\n')
            f.write(f'          <box><size>{thickness} {radius * angle_step:.3f} {height}</size></box>\n')
            f.write('        </geometry>\n')
            f.write('        <material><ambient>0.3 0.3 0.9 1</ambient></material>\n')
            f.write('      </visual>\n')
            f.write('    </link>\n')

        f.write('  </model>\n')
        f.write('</sdf>\n')

    print(f"S形墙模型已生成:{filename}")

# 运行脚本
generate_s_wall()
