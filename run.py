import os
import subprocess
import sys

def main():
    print(" Starting deployment initialization...")
    
    # 1. Rebuild the vector database from source PDFs if it doesn't exist
    if not os.path.exists("chroma_db") or len(os.listdir("chroma_db")) == 0:
        print(" Vector database cache empty. Seeding reference clinical knowledge...")
        try:
            subprocess.run([sys.executable, "make_samples.py"], check=True)
            print(" Vector database successfully initialized!")
        except subprocess.CalledProcessError as e:
            print(f" Failed to initialize vector database: {e}")
            sys.exit(1)
    else:
        print(" Existing vector database found. Skipping initialization.")

    # 2. Launch the Streamlit dashboard on the port specified by the cloud host
    port = os.environ.get("PORT", "8501")
    print(f" Launching Streamlit web application on port {port}...")
    
    #  Streams the text progress directly to your terminal screen
subprocess.run([sys.executable, "make_samples.py"], check=True, capture_output=False, text=True)

if __name__ == "__main__":
    main()