def main():
    try:
        total_sales = 0.0
        count = 0

        with open("sales_totals.txt", "r") as sales_file:
            for line in sales_file:
                line = line.strip()
                if line:  # Ensures the line is not empty
                    sale_amount = float(line)
                    total_sales += sale_amount
                    count += 1
                    print(f"Sale Amount: ${sale_amount:.2f}")

        if count > 0:
            average_sales = total_sales / count
            print(f"\nTotal Sales: ${total_sales:.2f}")
            print(f"Number of Entries: {count}")
            print(f"Average Sale Amount: ${average_sales:.2f}")
        else:
            print("No sales entries found.")

    except FileNotFoundError:
        print("Error: The file 'sales_totals.txt' was not found.")
    except ValueError:
        print("Error: There was a problem converting a line to a float.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
main()
