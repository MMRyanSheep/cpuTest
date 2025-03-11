#paoFen
import time, random, psutil, threading, math
import matplotlib.pyplot as plt
max_cpu = 0
max_cpu_time = None
stop_monitor = False
def arrGenerator(num):
    arr = [random.randint(0, num * 2) for i in range(num)]
    return arr
def test(func, data):
    start = time.time()
    func(data)
    end = time.time()
    score = (end - start) // 0.00000008
    return int(score)
def qucikSortTest(times):
    arr = arrGenerator(times)
    start = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    end = time.time()
    score = (end - start) // 0.00000008
    return int(score)
def intAdd(num):
    sum = 0
    for i in range(num):
        sum += i
    return sum
def bubble_sort(times):
    arr = arrGenerator(times)
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def floatAdd(num):
    sum = 0.0
    i = 3.1415926
    for c in range(num):
        sum += i
    return sum
def intDivide(num):
    sum = 1
    for i in range(1, num):
        sum /= i
    return sum
def single_partition_swap(arr, low, high):
    pivot = arr[low]  
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j
def quick_sort(arr, low, high):  
    if low < high:
        pivot_index = single_partition_swap(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    return arr
def monitor_cpu(interval=0.06):
    global max_cpu, max_cpu_time
    while not stop_monitor:
        cpu_percent = psutil.cpu_percent(interval=interval)
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        #print(f"[{current_time}] 当前 CPU 占用率: {cpu_percent}%")
        if cpu_percent > max_cpu:
            max_cpu = cpu_percent
            max_cpu_time = current_time
    #print("CPU 监控线程已停止。")
def create_multiple_donut_charts(data, max_score=100, labels=None, colors=None):
    num = len(data)
    if labels is None:
        labels = [f'项 {i+1}' for i in range(num)]
    if colors is None:
        colors = plt.cm.viridis([i/num for i in range(num)])
    
    # 计算每个子图的行数和列数
    cols = math.ceil(math.sqrt(num))
    rows = math.ceil(num / cols)
    
    fig, axes = plt.subplots(rows, cols, figsize=(cols * 4, rows * 4))
    axes = axes.flatten()  # 将二维数组展平以便迭代
    fig.suptitle('Result')
    fig.subplots_adjust(top=0.95)
    #fig.savefig('donut_charts.png')

    for i, (ax, value, label, color) in enumerate(zip(axes, data, labels, colors)):
        percentage = value / max_score * 100
        sizes = [percentage, 100 - percentage]
        wedge_colors = [color, '#e0e0e0']  # 主颜色和背景色
        wedges, _ = ax.pie(sizes, colors=wedge_colors, startangle=90, wedgeprops=dict(width=0.3))

        # 添加中心文本
        ax.text(0, 0, f'{value}', ha='center', va='center', fontsize=12)
        ax.set_title(label)

    # 隐藏多余的子图
    for j in range(i + 1, len(axes)):
        axes[j].axis('off')
    
    plt.tight_layout()
    plt.show()

cpu_thread = threading.Thread(target=monitor_cpu, daemon=True)
cpu_thread.start()
print("主线程正在运行...")
intTestScore = test(intAdd, 100000) * 3
floatTestScore = test(floatAdd, 100000) * 3
intDivideTestScore = test(intDivide, 100000) * 3
bubbleSortTestScore = test(bubble_sort, 1000) // 4
quickSortTestScore = qucikSortTest(10000)
score = intTestScore + floatTestScore + intDivideTestScore + quickSortTestScore + bubbleSortTestScore
print("yout CPU score is: ", score)
print('Details: ', '\n', 'intTestScore: ', intTestScore, '\n', 'floatTestScore: ', floatTestScore \
    , '\n', 'intDivideTestScore: ', intDivideTestScore, '\n', 'quickSortTestScore: ', quickSortTestScore \
    , '\n', 'bubbleSortTestScore: ', bubbleSortTestScore)
stop_monitor = True
cpu_thread.join()

if max_cpu_time:
    print(f"最高 CPU 占用率为 {max_cpu}%，发生在 {max_cpu_time}")
else:
    print("未记录到 CPU 占用率。")

data = [intTestScore, floatTestScore, intDivideTestScore, (quickSortTestScore + bubbleSortTestScore) / 2]
labels = ['intTestScore', 'floatTestScore', 'intDivideTestScore', 'sortTestScore']
create_multiple_donut_charts(data, max_score=score, labels=labels)