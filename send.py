import argparse


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Start Sending the program")

    parser.add_argument("--NOTION_KEY")
    parser.add_argument("--DATABASE_ID")
    parser.add_argument("--KAKAO_TOKEN")
    
    args = parser.parse_args()

    from plzread import Database, send_message

    db = Database()
    df = db.run(args.NOTION_KEY, args.DATABASE_ID)
    
    send_message(df, args.KAKAO_TOKEN)