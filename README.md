# Brain_MRI-Detection

\documentclass{article}
\usepackage{graphicx}
\usepackage{hyperref}

\title{MRI Detection with YOLO11}
\author{}
\date{}

\begin{document}

\maketitle

\section{Introduction}
This project is a Streamlit-based application that uses a YOLO11 model to detect MRI regions in medical images. Users can upload MRI images, and the model will identify and highlight relevant regions.

\section{Features}
\begin{itemize}
    \item Upload MRI images in JPG, JPEG, or PNG formats
    \item Perform object detection using a YOLO11 model
    \item Display detected MRI regions with bounding boxes
    \item Extract and show cropped MRI regions separately
    \item Adjustable confidence threshold for predictions
\end{itemize}

\section{Requirements}
Make sure you have the following dependencies installed:
\begin{verbatim}
streamlit
opencv-python
ultralytics
numpy
pillow
\end{verbatim}
You can install them using:
\begin{verbatim}
pip install -r requirements.txt
\end{verbatim}

\section{Installation and Setup}
\begin{enumerate}
    \item \textbf{Clone the repository (if applicable)}
    \begin{verbatim}
    git clone <your-repo-url>
    cd <your-repo-folder>
    \end{verbatim}
    \item \textbf{Set up a virtual environment (optional but recommended)}
    \begin{verbatim}
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate     # On Windows
    \end{verbatim}
    \item \textbf{Install dependencies}
    \begin{verbatim}
    pip install -r requirements.txt
    \end{verbatim}
    \item \textbf{Ensure you have the YOLO model file}
    \begin{itemize}
        \item Place \texttt{best.pt} in the project directory.
    \end{itemize}
\end{enumerate}

\section{Running the Application}
To start the Streamlit app, run:
\begin{verbatim}
streamlit run app.py
\end{verbatim}
This will open a browser window with the application interface.

\section{How It Works}
\begin{enumerate}
    \item Upload an MRI image.
    \item Adjust the confidence threshold if needed.
    \item The model detects MRI regions and highlights them with bounding boxes.
    \item Extracted regions are displayed separately for better visualization.
\end{enumerate}

\section{File Structure}
\begin{verbatim}
📂 Project Folder
├── app.py             # Main application script
├── best.pt            # Pre-trained YOLO model file
├── requirements.txt   # Required Python packages
\end{verbatim}

\section{Notes}
\begin{itemize}
    \item The model file (\texttt{best.pt}) must be in the same directory as \texttt{app.py}.
    \item The application requires a working internet connection to download model dependencies if not installed locally.
    \item Make sure your Python version is compatible (preferably Python 3.8+).
\end{itemize}


\end{document}

