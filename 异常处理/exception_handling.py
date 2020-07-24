if __name__ == "__main__":
    try:
        v = 1/0
    except ZeroDivisionError:
        print("error")
    finally:
        print("handled")

    print("end")