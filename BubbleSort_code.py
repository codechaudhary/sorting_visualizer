import time

def bubble_sort(data, draw_rectangle, delay):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            # Condition
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

                draw_rectangle(data, ['blue' if x == j or x == j+1 else 'red' for x in range(len(data))])
                time.sleep(delay)

    draw_rectangle(data, ['blue' for x in range(len(data))])
