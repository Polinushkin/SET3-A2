import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def load_csv_data(filename):
    try:
        data = pd.read_csv(filename)
        return data
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return None
    except Exception as e:
        print(f"Ошибка при загрузке {filename}: {e}")
        return None

def plot_merge_sort_comparison():
    random_data = load_csv_data('merge_sort_random.csv')
    reversed_data = load_csv_data('merge_sort_reversed.csv')
    nearly_sorted_data = load_csv_data('merge_sort_nearly_sorted.csv')

    if random_data is None or reversed_data is None or nearly_sorted_data is None:
        print("Нет данных для графика merge sort")
        return

    plt.figure(figsize=(10, 6))
    plt.plot(random_data['n'], random_data['time_us'], label='Random Array', marker='o', linestyle='-', markersize=3)
    plt.plot(reversed_data['n'], reversed_data['time_us'], label='Reversed Array', marker='s', linestyle='-', markersize=3)
    plt.plot(nearly_sorted_data['n'], nearly_sorted_data['time_us'], label='Nearly Sorted Array', marker='^', linestyle='-', markersize=3)
    plt.title("Merge sort Performance Comparison", fontsize=16)
    plt.xlabel("Array Size (n)", fontsize=14)
    plt.ylabel("Execution Time (microseconds)", fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig('merge_sort_comparison.png', dpi=300)
    plt.show()

def plot_hybrid_sort_comparison_single_threshold(threshold_idx=2):
    random_data = load_csv_data('hybrid_sort_random.csv')
    reversed_data = load_csv_data('hybrid_sort_reversed.csv')
    nearly_sorted_data = load_csv_data('hybrid_sort_nearly_sorted.csv')

    if random_data is None or reversed_data is None or nearly_sorted_data is None:
        print("Нет данных для графика hybrid sort")
        return

    thresholds = [5, 10, 15, 20, 30, 50]
    selected_threshold = thresholds[threshold_idx]
    time_col = f'time_us_th_{selected_threshold}'

    plt.figure(figsize=(10, 6))
    plt.plot(random_data['n'], random_data[time_col], label=f'Random Array (th={selected_threshold})', marker='o', linestyle='-', markersize=3)
    plt.plot(reversed_data['n'], reversed_data[time_col], label=f'Reversed Array (th={selected_threshold})', marker='s', linestyle='-', markersize=3)
    plt.plot(nearly_sorted_data['n'], nearly_sorted_data[time_col], label=f'Nearly Sorted Array (th={selected_threshold})', marker='^', linestyle='-', markersize=3)
    plt.title(f"Hybrid merge+insertion sort Performance (threshold = {selected_threshold})", fontsize=16)
    plt.xlabel("Array Size", fontsize=14)
    plt.ylabel("Execution Time (microseconds)", fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(f'hybrid_sort_comparison_th_{selected_threshold}.png', dpi=300)
    plt.show()

def plot_hybrid_threshold_comparison(array_type='random'):
    filename_map = {
        'random': 'hybrid_sort_random.csv',
        'reversed': 'hybrid_sort_reversed.csv',
        'nearly_sorted': 'hybrid_sort_nearly_sorted.csv'
    }
    filename = filename_map.get(array_type)
    data = load_csv_data(filename)
    if data is None:
        print(f"Нет данных для графика для {array_type}")
        return

    thresholds = [5, 10, 15, 20, 30, 50]
    plt.figure(figsize=(10, 6))
    for th in thresholds:
        time_col = f'time_us_th_{th}'
        plt.plot(data['n'], data[time_col], label=f'Threshold {th}', linestyle='-', marker='.', markersize=2)

    plt.title(f"Hybrid Sort Performance Comparison\n({array_type.replace('_', ' ').title()} Array)", fontsize=16)
    plt.xlabel("Array Size", fontsize=14)
    plt.ylabel("Execution Time (microseconds)", fontsize=14)
    plt.legend(fontsize=10, loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(f'hybrid_threshold_comparison_{array_type}.png', dpi=300)
    plt.show()

def plot_all_hybrid_thresholds():
    fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)
    array_types = ['random', 'reversed', 'nearly_sorted']
    filenames = ['hybrid_sort_random.csv', 'hybrid_sort_reversed.csv', 'hybrid_sort_nearly_sorted.csv']
    titles = ['Random Array', 'Reversed Array', 'Nearly Sorted Array']
    thresholds = [5, 10, 15, 20, 30, 50]

    for i, (ax, array_type, filename, title) in enumerate(zip(axes, array_types, filenames, titles)):
        data = load_csv_data(filename)
        if data is None:
            print(f"Нет данных для подграфика для {array_type}")
            continue

        for th in thresholds:
            time_col = f'time_us_th_{th}'
            ax.plot(data['n'], data[time_col], label=f'Th {th}', linestyle='-', marker='.', markersize=1.5)

        ax.set_title(f"{title}", fontsize=14)
        ax.set_xlabel("Array Size", fontsize=12)
        if i == 0:
            ax.set_ylabel("Execution Time (microseconds)", fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend(fontsize=8, loc='upper left')

    plt.suptitle("Hybrid Sort Performance - effect of threshold", fontsize=16)
    plt.tight_layout()
    plt.savefig('hybrid_threshold_comparison_all.png', dpi=300)
    plt.show()

def plot_merge_individual_from_csv():
    random_data = load_csv_data('merge_sort_random.csv')
    reversed_data = load_csv_data('merge_sort_reversed.csv')
    nearly_sorted_data = load_csv_data('merge_sort_nearly_sorted.csv')

    plt.figure(figsize=(10, 6))
    plt.plot(random_data['n'], random_data['time_us'], marker='o', linestyle='-', markersize=3)
    plt.title("Merge sort Performance - Random Array", fontsize=16)
    plt.xlabel("Array Size (n)", fontsize=14)
    plt.ylabel("Execution Time (microseconds)", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig('merge_sort_random.png', dpi=300)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(reversed_data['n'], reversed_data['time_us'], marker='s', linestyle='-', markersize=3, color='orange')
    plt.title("Merge sort Performance - Reversed Array", fontsize=16)
    plt.xlabel("Array Size (n)", fontsize=14)
    plt.ylabel("Execution Time (microseconds)", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig('merge_sort_reversed.png', dpi=300)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(nearly_sorted_data['n'], nearly_sorted_data['time_us'], marker='^', linestyle='-', markersize=3, color='green')
    plt.title("Merge sort Performance - Nearly Sorted Array", fontsize=16)
    plt.xlabel("Array Size (n)", fontsize=14)
    plt.ylabel("Execution Time (microseconds)", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig('merge_sort_nearly_sorted.png', dpi=300)
    plt.show()


if __name__ == "__main__":
    plot_merge_sort_comparison()
    plot_merge_individual_from_csv()
    plot_hybrid_sort_comparison_single_threshold(threshold_idx=2)
    plot_hybrid_threshold_comparison('random')
    plot_hybrid_threshold_comparison('reversed')
    plot_hybrid_threshold_comparison('nearly_sorted')
    plot_all_hybrid_thresholds()
    print("Все графики построены и сохранены ")
