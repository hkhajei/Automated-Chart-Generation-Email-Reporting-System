import scripts.generate_charts as gc
import scripts.send_email as se

def run():
    print("Generating charts...")
    gc.generate_sample_charts()
    print("Sending emails...")
    se.main()
    print("Process completed.")

if __name__ == "__main__":
    run()

