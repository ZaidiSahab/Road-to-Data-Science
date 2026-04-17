# import streamlit as st
# import pandas as pd
# import plotly.express as px

# st.title("Book Data Dashboard")
# df = pd.read_csv("Books_Data_Clean.csv")

# # Fix column names (you already did this, but just in case)
# df.columns = df.columns.str.lower().str.replace(' ', '_')

# # Filters
# genre = st.selectbox("Select Genre", df['genre'].unique())
# min_y = int(df['publishing_year'].min())
# max_y = int(df['publishing_year'].max())
# year = st.slider("Publishing Year", min_y, max_y, (min_y, max_y))

# # Filter data
# filtered = df[(df['publishing_year'] >= year[0]) & (df['publishing_year'] <= year[1]) & (df['genre'] == genre)]

# st.write(f"Books in {genre}, {year[0]}-{year[1]}: {len(filtered)}")

# # Plots
# fig = px.bar(filtered, x='author', y='book_average_rating', title='Avg Rating by Author')
# st.plotly_chart(fig)

# st.write("Top Publishers by Revenue")
# st.dataframe(df.groupby('publisher')['publisher_revenue'].sum().sort_values(ascending=False).head(10))


# year = st.slider("Publishing Year", 
#                  int(df['publishing_year'].min()), 
#                  int(df['publishing_year'].max()), 
#                  (int(1900), int(2020)))







 
######################  2nd Attempt Now Lets see ######################



######################











# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# # Page Configuration
# st.set_page_config(page_title="Book Data Insights", layout="wide")

# # Custom CSS for UI Enhancement
# st.markdown("""
#     <style>
#     .main {
#         background-color: #f5f7f9;
#     }
#     .stMetric {
#         background-color: #ffffff;
#         padding: 15px;
#         border-radius: 10px;
#         box-shadow: 0 2px 4px rgba(0,0,0,0.05);
#     }
#     </style>
#     """, unsafe_allow_html=True)

# @st.cache_data
# def load_data():
#     df = pd.read_csv("Books_Data_Clean.csv")
#     # Clean column names to be lowercase and underscore-friendly
#     df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
#     # Filter for years > 1900 as per your logic
#     df = df[df["publishing_year"] > 1900]
#     # Drop rows without a Book Name
#     df.dropna(subset=["book_name"], inplace=True)
#     return df

# try:
#     df = load_data()

#     # --- SIDEBAR FILTERS ---
#     st.sidebar.header("Dashboard Filters")
    
#     genres = st.sidebar.multiselect(
#         "Select Genres", 
#         options=df['genre'].unique(), 
#         default=df['genre'].unique()[:5]
#     )
    
#     year_range = st.sidebar.slider(
#         "Publishing Year Range",
#         min_value=int(df['publishing_year'].min()),
#         max_value=int(df['publishing_year'].max()),
#         value=(1900, int(df['publishing_year'].max()))
#     )

#     # Filter Dataframe
#     mask = (df['genre'].isin(genres)) & \
#            (df['publishing_year'].between(year_range[0], year_range[1]))
#     filtered_df = df[mask]

#     # --- MAIN UI ---
#     st.title("📚 Book Data Analytics Dashboard")
#     st.markdown("Exploring trends in publishing, sales, and ratings.")

#     # Top Metrics Row
#     col1, col2, col3, col4 = st.columns(4)
#     col1.metric("Total Books", f"{len(filtered_df)}")
#     col2.metric("Avg Rating", f"{filtered_df['book_average_rating'].mean():.2f} ⭐")
#     col3.metric("Total Revenue", f"${filtered_df['publisher_revenue'].sum():,.0f}")
#     col4.metric("Units Sold", f"{filtered_df['units_sold'].sum():,.0f}")

#     st.divider()

#     # --- ROW 1: Distribution & Genres ---
#     row1_col1, row1_col2 = st.columns(2)

#     with row1_col1:
#         st.subheader("Distribution of Publishing Years")
#         fig_hist = px.histogram(filtered_df, x="publishing_year", nbins=30, 
#                                 color_discrete_sequence=['#636EFA'],
#                                 labels={'publishing_year': 'Year'})
#         st.plotly_chart(fig_hist, use_container_width=True)

#     with row1_col2:
#         st.subheader("Books per Genre")
#         genre_counts = filtered_df['genre'].value_counts().reset_index()
#         fig_bar = px.bar(genre_counts, x='genre', y='count', 
#                          color='genre', color_discrete_sequence=px.colors.qualitative.Pastel)
#         st.plotly_chart(fig_bar, use_container_width=True)

#     # --- ROW 2: Ratings & Sales ---
#     row2_col1, row2_col2 = st.columns(2)

#     with row2_col1:
#         st.subheader("Ratings Count by Genre (Outliers)")
#         fig_box = px.box(filtered_df, x='genre', y='book_ratings_count', 
#                          color='genre', title="Book Ratings Count by Genre")
#         st.plotly_chart(fig_box, use_container_width=True)

#     with row2_col2:
#         st.subheader("Price vs Units Sold")
#         fig_scatter = px.scatter(filtered_df, x='sale_price', y='units_sold', 
#                                  size='book_average_rating', color='genre',
#                                  hover_name='book_name', opacity=0.7)
#         st.plotly_chart(fig_scatter, use_container_width=True)

#     # --- ROW 3: Revenue & Languages ---
#     row3_col1, row3_col2 = st.columns([2, 1])

#     with row3_col1:
#         st.subheader("Top Publishers by Revenue")
#         top_publishers = filtered_df.groupby('publisher')['publisher_revenue'].sum().sort_values(ascending=False).head(10).reset_index()
#         fig_rev = px.bar(top_publishers, x='publisher_revenue', y='publisher', orientation='h',
#                          color='publisher_revenue', color_continuous_scale='Viridis')
#         st.plotly_chart(fig_rev, use_container_width=True)

#     with row3_col2:
#         st.subheader("Language Distribution")
#         lang_counts = filtered_df['language_code'].value_counts().reset_index()
#         fig_pie = px.pie(lang_counts, values='count', names='language_code', hole=0.4)
#         st.plotly_chart(fig_pie, use_container_width=True)

#     # --- DATA TABLE ---
#     with st.expander("View Raw Filtered Data"):
#         st.dataframe(filtered_df, use_container_width=True)

# except FileNotFoundError:
#     st.error("CSV file not found. Please ensure 'Books_Data_Clean.csv' is in the same directory.")
# except Exception as e:
#     st.error(f"An error occurred: {e}")









###################### 3rd Attempt ##############################
# 
# 
# 
# 
# ####################################


import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Config
st.set_page_config(page_title="Book Data Analysis", layout="wide")

# 2. Stable CSS for Visibility (Fixes Dark/Light Mode issues)
st.markdown("""
    <style>
    /* Metric Card Styling - Works in both Light and Dark Mode */
    [data-testid="stMetricValue"] {
        font-size: 28px;
        font-weight: bold;
        color: #007bff !important;
    }
    [data-testid="stMetricLabel"] {
        font-size: 16px;
        font-weight: 500;
    }
    /* Chart container styling */
    .plot-container {
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data
def load_and_clean_data():
    df = pd.read_csv("Books_Data_Clean.csv")
    # Clean column names for coding ease
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    # Your core logic: Filter years > 1900 and drop missing names
    df = df[df["publishing_year"] > 1900]
    df.dropna(subset=["book_name"], inplace=True)
    return df

try:
    df = load_and_clean_data()

    # --- SIDEBAR CONTROLS ---
    st.sidebar.header("Dashboard Filters")
    
    # User-Friendly Year Range (Select Slider)
    years = sorted(df['publishing_year'].unique().astype(int))
    start_year, end_year = st.sidebar.select_slider(
        "Select Publishing Period",
        options=years,
        value=(min(years), max(years))
    )

    # Genre Filter
    all_genres = sorted(df['genre'].unique())
    selected_genres = st.sidebar.multiselect("Select Genres", all_genres, default=all_genres[:5])

    # Apply Filters
    filtered_df = df[
        (df['publishing_year'].between(start_year, end_year)) & 
        (df['genre'].isin(selected_genres))
    ]

    # --- HEADER SECTION ---
    st.title("📊 Book Industry Analysis Dashboard")
    st.markdown("---")

    # Key Metrics (Legible in all modes)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Books", f"{len(filtered_df):,}")
    m2.metric("Avg Rating", f"{filtered_df['book_average_rating'].mean():.2f} / 5")
    m3.metric("Total Revenue", f"${filtered_df['publisher_revenue'].sum():,.0f}")
    m4.metric("Units Sold", f"{filtered_df['units_sold'].sum():,.0f}")

    st.markdown("---")

    # --- ROW 1: HISTOGRAM & BAR CHART ---
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Distribution of Publishing Year")
        fig1 = px.histogram(filtered_df, x='publishing_year', nbins=20, 
                           labels={'publishing_year': 'Year', 'count': 'Frequency'},
                           color_discrete_sequence=['#007bff'])
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("Books in Each Genre")
        genre_counts = filtered_df['genre'].value_counts().reset_index()
        fig2 = px.bar(genre_counts, x='genre', y='count', 
                     color='genre', color_discrete_sequence=px.colors.qualitative.Safe)
        st.plotly_chart(fig2, use_container_width=True)

    # --- ROW 2: RATINGS BY AUTHOR & BOX PLOT ---
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Top Authors by Avg Rating")
        top_authors = filtered_df.groupby('author')['book_average_rating'].mean().sort_values(ascending=False).head(10).reset_index()
        fig3 = px.bar(top_authors, x='book_average_rating', y='author', orientation='h',
                     color='book_average_rating', color_continuous_scale='Blues')
        st.plotly_chart(fig3, use_container_width=True)

    with col4:
        st.subheader("Ratings Count by Genre (Box Plot)")
        fig4 = px.box(filtered_df, x='genre', y='book_ratings_count', color='genre')
        st.plotly_chart(fig4, use_container_width=True)

    # --- ROW 3: SCATTER PLOT & PIE CHART ---
    col5, col6 = st.columns([2, 1])

    with col5:
        st.subheader("Sale Price vs Units Sold")
        fig5 = px.scatter(filtered_df, x='sale_price', y='units_sold', 
                         color='genre', size='book_average_rating',
                         hover_name='book_name')
        st.plotly_chart(fig5, use_container_width=True)

    with col6:
        st.subheader("Language Distribution")
        fig6 = px.pie(filtered_df, names='language_code', hole=0.3)
        st.plotly_chart(fig6, use_container_width=True)

    # --- ROW 4: REVENUE BY PUBLISHER ---
    st.markdown("---")
    st.subheader("Publisher Performance (Total Revenue)")
    pub_rev = filtered_df.groupby('publisher')['publisher_revenue'].sum().sort_values(ascending=False).head(15).reset_index()
    fig7 = px.bar(pub_rev, x='publisher', y='publisher_revenue', color='publisher_revenue', color_continuous_scale='Viridis')
    st.plotly_chart(fig7, use_container_width=True)

    # --- DATA TABLE ---
    with st.expander("View Full Data Audit"):
        st.dataframe(filtered_df, use_container_width=True)

except Exception as e:
    st.error(f"Error loading dashboard: {e}")
    st.info("Check if your CSV file column names match the script.")