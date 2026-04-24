def show_map():
    import streamlit as st

    import streamlit as st
    import pandas as pd
    import mysql.connector
    import plotly.express as px
    import json

    
    # STYLE
    
    st.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        background-color: #0b0b2b;
    }
    div[data-baseweb="select"] span {
        color: black !important;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    div[data-testid="stVerticalBlock"] > div {
        margin-bottom: 10px;
    }
    [data-testid="column"] {
        padding: 0px 10px !important;
    }
    h3, h4 {
        margin-bottom: 5px !important;
    }


    div[data-testid="column"] {
        display: flex;
        flex-direction: column;
    }

    /* Make children fill full height */
    div[data-testid="column"] > div {
        flex-grow: 1;
    }

    /* Make plot fill full column */
    .js-plotly-plot {
        height: 100% !important;
    }


    </style>
    """, unsafe_allow_html=True)

    st.set_page_config(layout="wide")

    
    # DB CONNECTION
    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Annusingh123@",
        database="phonepe_db"
    )

    
    # LOAD GEOJSON
    
    with open("india_states.geojson") as f:
        india_geo = json.load(f)

    geo_key = list(india_geo["features"][0]["properties"].keys())[0]

    for feature in india_geo["features"]:
        feature["properties"][geo_key] = str(feature["properties"][geo_key]).strip().title()

    
    # SIDEBAR
    
    with st.sidebar:
        st.markdown("### All India")

        analysis_type = st.selectbox("", ["Transactions", "Users"], label_visibility="collapsed")

        table = "aggregated_transaction" if analysis_type == "Transactions" else "aggregated_user"

        year_query = f"SELECT DISTINCT year FROM {table} ORDER BY year DESC"
        years = pd.read_sql(year_query, conn)['year'].tolist()
        year = st.selectbox("", years, label_visibility="collapsed")

        q_query = f"""
        SELECT DISTINCT quarter FROM {table}
        WHERE year = {year}
        ORDER BY quarter
        """
        quarters = pd.read_sql(q_query, conn)['quarter'].tolist()
        quarter = st.selectbox("", quarters, label_visibility="collapsed")

        
    
    # MAIN QUERY
    
    if analysis_type == "Transactions":
        query = f"""
        SELECT state, SUM(transaction_amount) AS value
        FROM aggregated_transaction
        WHERE year={year} AND quarter={quarter}
        GROUP BY state
        """
    else:
        query = f"""
        SELECT state, SUM(user_count) AS value
        FROM aggregated_user
        WHERE year={year} AND quarter={quarter}
        GROUP BY state
        """

    df = pd.read_sql(query, conn)

    
    # CLEAN STATE NAMES
    
    state_mapping = {
        "Andaman & Nicobar Islands": "Andaman And Nicobar",
        "Dadra & Nagar Haveli & Daman & Diu": "Dadra And Nagar Haveli And Daman And Diu",
        "Delhi": "Nct Of Delhi"
    }

    df["state"] = df["state"].replace(state_mapping)
    df["state"] = df["state"].str.strip().str.title()

    
    # FALLBACK DATA
    
    st.write("Rows fetched:", len(df))

    if df.empty or len(df) < 5:
        st.warning("⚠️ Data not available. Showing latest available data.")

        if analysis_type == "Transactions":
            fallback_query = "SELECT state, SUM(transaction_amount) AS value FROM aggregated_transaction GROUP BY state"
        else:
            fallback_query = "SELECT state, SUM(user_count) AS value FROM aggregated_user GROUP BY state"

        df = pd.read_sql(fallback_query, conn)

    df["state"] = df["state"].str.strip().str.title()

    
    # LAYOUT
    
    col1, col2 = st.columns([3.5, 1.2])

    
    # MAP
    
    with col1:
        st.markdown("## 📊 PhonePe Pulse Dashboard")

        fig = px.choropleth(
            df,
            geojson=india_geo,
            locations="state",
            featureidkey="properties.NAME_1",
            color="value",
            color_continuous_scale="Plasma",
        )

        fig.update_geos(fitbounds="locations", visible=False)

        fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=0, b=0),
        )

        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    
    # RIGHT PANEL
   
    with col2:

        st.markdown("""
        <style>
        .card {
            background: #1e1b2e;
            padding: 18px;
            border-radius: 12px;
            color: white;
            margin-bottom: 15px;
        }
        .title { font-size: 14px; color: #94a3b8; }
        .big-number { font-size: 20px; font-weight: 200; }
        .section-title { font-size: 16px; font-weight: 600; margin-top: 10px; }
        .row {
            display: flex;
            justify-content: space-between;
            font-size: 13px;
            padding: 4px 0;
        }
        </style>
        """, unsafe_allow_html=True)

        # TOTAL
        total_value = int(df["value"].sum())

        st.markdown(f"""
        <div class="card">
            <div class="title">{analysis_type}</div>
            <div class="big-number">₹ {total_value:,}</div>
            <div class="title">All India Total</div>
        </div>
        """, unsafe_allow_html=True)

        tabs = st.tabs(["🏆 Top States", "📊 Categories", "📍 Districts"])

    
    # TOP STATES
    
    with tabs[0]:
        top_states = df.sort_values("value", ascending=False).head(10)

        for _, row in top_states.iterrows():
            st.markdown(f"""
            <div class="row">
                <span>{row['state']}</span>
                <span style="color:#22c55e;">₹ {int(row['value']):,}</span>
            </div>
            """, unsafe_allow_html=True)


    
    # CATEGORIES
    
    with tabs[1]:
        if analysis_type == "Transactions":

            q2 = f"""
            SELECT transaction_type,
                SUM(transaction_amount) AS total
            FROM aggregated_transaction
            WHERE year={year} AND quarter={quarter}
            GROUP BY transaction_type
            """

            cat_df = pd.read_sql(q2, conn)

            for _, row in cat_df.iterrows():
                st.markdown(f"""
                <div class="row">
                    <span>{row['transaction_type']}</span>
                    <span style="color:#38bdf8;">₹ {int(row['total']):,}</span>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("Categories available only for Transactions")


    
    # DISTRICTS
    
    with tabs[2]:
        try:
            q3 = f"""
            SELECT district,
                SUM(transaction_amount) AS total
            FROM map_transaction_district
            WHERE year={year} AND quarter={quarter}
            GROUP BY district
            ORDER BY total DESC
            LIMIT 5
            """

            district_df = pd.read_sql(q3, conn)

            for _, row in district_df.iterrows():
                st.markdown(f"""
                <div class="row">
                    <span>{row['district']}</span>
                    <span style="color:#facc15;">₹ {int(row['total']):,}</span>
                </div>
                """, unsafe_allow_html=True)

        except:
            st.write("No district data available")
    
    # CLOSE DB
    # ===============================================================================#
    conn.close()