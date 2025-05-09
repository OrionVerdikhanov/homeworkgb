class ListComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def average(self, numbers):
        return sum(numbers) / len(numbers)

    def compare_averages(self):
        avg1 = self.average(self.list1)
        avg2 = self.average(self.list2)
        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        if avg2 > avg1:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python comparator.py <comma-separated-numbers1> <comma-separated-numbers2>")
        sys.exit(1)
    list1 = list(map(float, sys.argv[1].split(",")))
    list2 = list(map(float, sys.argv[2].split(",")))
    comparator = ListComparator(list1, list2)
    print(comparator.compare_averages())
