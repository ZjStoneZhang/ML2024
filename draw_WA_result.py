import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

wa_cnn = [
    [  # top-1 accuracy
        [81.3, 72.9, 67.65, 62.42, 58.31],                                    # 0  + 5*20
        [89.9, 77.85, 74.03, 69.1, 65.36, 61.87, 61.2, 57.28, 55.09, 52.83],  # 0  + 10*10
        [76.32, 68.77, 65.47, 61.09, 58.54, 56.36]                            # 50 + 5*10
    ],
    [  # top-5 accuracy
        [96.95, 94.08, 90.93, 87.95, 85.66],
        [99.8, 95.9, 94.07, 92.4, 90.46, 88.6, 86.83, 85.21, 83.47, 82.16],
        [94.46, 90.97, 88.39, 86.28, 84.6, 83.46]
    ]
]

wa_nme = [  # same order as the above
    [
        [81.45, 72.85, 66.68, 61.01, 56.29],
        [89.3, 78.25, 74.17, 68.18, 64.4, 61.13, 59.11, 55.21, 52.67, 50.94],
        [76.04, 69.5, 65.26, 60.95, 57.29, 54.88]
    ],
    [
        [96.9, 93.82, 90.0, 86.65, 83.7],
        [99.7, 96.4, 94.33, 91.7, 89.76, 86.95, 85.14, 82.71, 80.18, 78.3],
        [94.66, 90.87, 88.86, 86.74, 84.51, 82.78]
    ]
]

icarl_cnn = [
    [
        [81.3, 70.85, 61.55, 52.16, 45.8],
        [89.0, 76.25, 70.4, 63.88, 58.6, 54.08, 51.71, 46.69, 43.82, 40.53],
        [75.92, 59.97, 56.24, 48.79, 45.68, 44.04]
    ],
    [
        [96.95, 93.55, 88.13, 83.34, 77.82],
        [99.2, 95.95, 93.03, 90.55, 86.7, 83.62, 80.31, 76.85, 74.92, 71.44],
        [94.44, 89.65, 85.49, 81.26, 77.09, 74.32]
    ]
]

icarl_nme = [
    [
        [81.45, 72.58, 66.27, 59.75, 54.68],
        [89.2, 76.6, 73.2, 68.08, 64.0, 59.85, 57.61, 53.3, 50.02, 49.11],
        [75.34, 65.25, 62.11, 56.26, 53.03, 51.15]
    ],
    [
        [96.9, 93.25, 89.1, 86.14, 82.36],
        [99.3, 95.2, 93.5, 91.3, 88.48, 86.03, 83.67, 81.18, 78.82, 77.09],
        [94.86, 89.78, 87.64, 85.04, 81.13, 79.84]
    ]
]

bic_cnn = [
    [
        [78.2, 70.97, 65.13, 59.59, 46.23],
        [88.0, 73.6, 71.1, 63.92, 61.98, 58.87, 57.09, 48.19, 45.11, 44.39],
        [76.68, 62.5, 58.01, 49.65, 42.12, 36.53]
    ],
    [
        [96.4, 92.95, 90.0, 87.15, 68.96],
        [99.2, 95.1, 92.7, 89.8, 88.72, 86.52, 84.87, 73.25, 71.66, 71.04],
        [94.3, 78.22, 77.99, 67.59, 59.07, 52.17]
    ]
]

bic_nme = [
    [
        [78.35, 70.65, 63.88, 59.24, 54.47],
        [87.7, 74.1, 70.9, 64.47, 62.22, 59.15, 57.01, 53.48, 49.83, 48.13],
        [75.2, 69.17, 62.29, 57.38, 53.22, 47.75]
    ],
    [
        [96.6, 93.22, 89.73, 86.5, 83.37],
        [99.0, 95.55, 92.87, 90.12, 88.38, 85.55, 83.59, 81.4, 78.19, 76.14],
        [94.12, 91.33, 87.19, 84.91, 80.97, 75.21]
    ]
]

replay_cnn = [
    [
        [80.65, 68.12, 57.85, 48.96, 44.14],
        [87.9, 74.45, 68.53, 59.48, 55.58, 51.18, 48.17, 43.2, 41.82, 39.86],
        [76.56, 52.47, 50.0, 45.19, 42.98, 41.02]
    ],
    [
        [96.95, 92.28, 85.78, 81.36, 76.82],
        [99.5, 94.65, 91.9, 87.72, 84.5, 81.23, 78.39, 76.24, 74.19, 71.7],
        [94.32, 83.2, 80.41, 77.97, 74.3, 72.9]
    ]
]

replay_nme = [
    [
        [80.9, 69.6, 61.55, 54.42, 49.39],
        [88.2, 75.35, 70.47, 63.78, 59.8, 56.48, 53.2, 49.24, 47.62, 45.36],
        [75.92, 54.37, 54.4, 51.05, 48.29, 46.66]
    ],
    [
        [97.0, 92.72, 87.88, 84.05, 79.89],
        [99.3, 94.75, 93.37, 89.08, 86.9, 83.72, 81.31, 79.03, 77.47, 75.22],
        [94.58, 84.08, 82.84, 80.31, 78.09, 75.91]
    ]
]

strategy = [
    [20, 40, 60, 80, 100],
    [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    [50, 60, 70, 80, 90, 100]
]

finetune_cnn = [
    [
        [81.3, 43.05, 28.42, 21.2, 17.13],
        [89.9, 39.55, 31.0, 21.85, 18.86, 14.85, 13.04, 11.19, 10.37, 8.92],
        [75.92, 14.83, 13.3, 11.18, 10.4, 8.84]
    ],
    [
        [96.95, 62.55, 47.47, 37.17, 29.28],
        [99.8, 73.75, 58.6, 50.6, 43.0, 35.37, 28.36, 24.42, 23.1, 18.57],
        [94.44, 37.18, 26.83, 26.14, 23.41, 19.16]
    ]
]


def average_acc(i):
    """
        acc_order: finetune -> replay -> bic -> icarl -> wa
    """
    acc = list()
    for j in range(3):
        cnn_acc = list()
        cnn_acc.append(sum(finetune_cnn[i][j]) / len(finetune_cnn[i][j]))
        cnn_acc.append(sum(replay_cnn[i][j]) / len(replay_cnn[i][j]))
        cnn_acc.append(sum(bic_cnn[i][j]) / len(bic_cnn[i][j]))
        cnn_acc.append(sum(icarl_cnn[i][j]) / len(icarl_cnn[i][j]))
        cnn_acc.append(sum(wa_cnn[i][j]) / len(wa_cnn[i][j]))
        acc.append(cnn_acc)

    print(acc)


def wa_average_acc(i):
    wa_cnn_acc = list()
    wa_nme_acc = list()
    for j in range(3):
        wa_cnn_acc.append(sum(wa_cnn[i][j]) / len(wa_cnn[i][j]))
        wa_nme_acc.append(sum(wa_nme[i][j]) / len(wa_nme[i][j]))
    print(wa_cnn_acc)
    print(wa_nme_acc)


def draw(i, option=False):
    # i=0: top-1 accuracy
    # i=1: top-5 accuracy
    for j in range(3):
        # 全局设置字体为 Times New Roman
        rcParams['font.family'] = 'Times New Roman'

        # 绘图
        fig, ax = plt.subplots(figsize=(4, 3))

        if option:
            ax.plot(strategy[j], wa_nme[i][j], label='NME', color=(239 / 255, 132 / 255, 39 / 255), linewidth=2)
            ax.scatter(strategy[j], wa_nme[i][j], color=(239 / 255, 132 / 255, 39 / 255), s=30, marker='s', facecolors='none', linewidths=2)
            ax.plot(strategy[j], wa_cnn[i][j], label='CNN', color=(0 / 255, 173 / 255, 246 / 255), linewidth=2)
            ax.scatter(strategy[j], wa_cnn[i][j], color=(0 / 255, 173 / 255, 246 / 255), s=30, marker='o', facecolors='none', linewidths=2)

        else:
            ax.plot(strategy[j], finetune_cnn[i][j], label='finetune', color=(128 / 255, 128 / 255, 128 / 255), linewidth=2)
            ax.scatter(strategy[j], finetune_cnn[i][j], color=(128 / 255, 128 / 255, 128 / 255), s=30, marker='.', linewidths=2)

            ax.plot(strategy[j], replay_cnn[i][j], label='replay', color=(128 / 255, 0 / 255, 0 / 255), linewidth=2)
            ax.scatter(strategy[j], replay_cnn[i][j], color=(128 / 255, 0 / 255, 0 / 255), s=30, marker='.', linewidths=2)

            ax.plot(strategy[j], icarl_cnn[i][j], label='iCaRL', color=(0 / 255, 128 / 255, 128 / 255), linewidth=2)
            ax.scatter(strategy[j], icarl_cnn[i][j], color=(0 / 255, 128 / 255, 128 / 255), s=30, marker='.', linewidths=2)

            ax.plot(strategy[j], bic_cnn[i][j], label='BiC', color=(255 / 255, 127 / 255, 80 / 255), linewidth=2)
            ax.scatter(strategy[j], bic_cnn[i][j], color=(255 / 255, 127 / 255, 80 / 255), s=30, marker='.', linewidths=2)

            ax.plot(strategy[j], wa_cnn[i][j], label='WA', color=(191 / 255, 0 / 255, 191 / 255), linewidth=2)
            ax.scatter(strategy[j], wa_cnn[i][j], color=(191 / 255, 0 / 255, 191 / 255), s=30, marker='.', linewidths=2)



        # 设置横坐标和纵坐标名称
        ax.set_xlabel('Number of classes', fontsize=12, fontweight='bold')
        ax.set_ylabel('Accuracy (%)', fontsize=12, fontweight='bold')

        # 设置横坐标的刻度和网格
        ax.set_xticks(np.arange(0, 101, 20))
        ax.set_xticklabels(np.arange(0, 101, 20), fontsize=12, fontweight='bold')
        ax.xaxis.grid(True, which='major', linestyle='--', color='grey', linewidth=1.0)

        # 设置纵坐标的刻度和网格
        ax.set_yticks(np.arange(0, 101, 10))
        ax.set_yticklabels(np.arange(0, 101, 10), fontsize=12, fontweight='bold')
        ax.yaxis.grid(True, which='major', linestyle='--', color='grey', linewidth=1.0)

        # 设置刻度线的粗细
        ax.tick_params(axis='x', which='major', width=1.5)
        ax.tick_params(axis='y', width=1.5)

        # 设置坐标的范围
        ax.set_xlim(0, 105)
        ax.set_ylim(0, 105)

        # 设置坐标轴线的粗细
        ax.spines['top'].set_linewidth(1.5)  # 上边框
        ax.spines['right'].set_linewidth(1.5)  # 右边框
        ax.spines['bottom'].set_linewidth(1.5)  # 下边框
        ax.spines['left'].set_linewidth(1.5)  # 左边框

        # 调整布局以避免标签被截断
        plt.tight_layout(pad=1.0)

        # 添加图例
        if j == 0 and i == 0:
            ax.legend(prop={'weight': 'bold', 'size': 10})

        # 显示图形
        plt.show()


if __name__ == '__main__':
    for i in range(2):
        draw(i)
        wa_average_acc(i)
        average_acc(i)
