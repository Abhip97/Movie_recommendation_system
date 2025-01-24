# Movie Recommendation System

## Overview
This project is a **Content-Based Movie Recommendation System** built using Python and Streamlit. It recommends similar movies based on a selected movie by analyzing a pre-trained similarity model and provides movie posters using the TMDb API.

## Features
- Select a movie from a dropdown list.
- Get recommendations for 5 similar movies.
- Display movie posters fetched dynamically from TMDb.

## Project Structure
```
movie-recommendation-system/
├── movies.pkl                # Pickle file containing movie data (titles, IDs, etc.)
├── similarity1.pkl           # Pickle file containing the similarity matrix
├── movie_app.py              # Streamlit application file
├── Movie_rec_system.ipynb    # Jupyter notebook used to create the model
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
```

## Prerequisites
- Python 3.8 or later
- TMDb API key (create an account at [TMDb](https://www.themoviedb.org/) to get an API key)

## dataset
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your TMDb API key:
   - Replace the placeholder API key in `movie_app.py` with your TMDb API key:
     ```python
     api_key = "YOUR_API_KEY"
     ```

## Running the Application
1. Run the Streamlit app:
   ```bash
   streamlit run movie_app.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

## How It Works
1. Select a movie from the dropdown menu.
2. Click the **Recommend** button.
3. The app uses a pre-trained content-based similarity model to find similar movies.
4. Movie posters are fetched from the TMDb API and displayed alongside the recommendations.

## Project Development
- **Model Creation**:
  The model was created using a Jupyter Notebook. You can find the notebook in the file `Movie_rec_system.ipynb`.
- **Application Development**:
  The Streamlit app was developed using PyCharm and is implemented in the file `movie_app.py`.

## Dependencies
- Python 3.8+
- Streamlit
- Requests

Install all dependencies with:
```bash
pip install -r requirements.txt
```

