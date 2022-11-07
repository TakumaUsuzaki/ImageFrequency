from image_frequency import image_frequency

if __name__ == '__main__':
    image_path = input("Please input the image file path: ")
    freq = image_frequency(image_path)
    print('Image frequency for column: {}'.format(
        freq.correlation_coefficient_column()))
    print('Image frequency for column: {}'.format(
        freq.correlation_coefficient_column()))
