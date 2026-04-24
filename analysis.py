def show_analysis():
    import streamlit as st
    import streamlit as st
    import pandas as pd
    import mysql.connector
    import plotly.express as px

    # ---------------- PAGE CONFIG ----------------
    st.set_page_config(page_title="PhonePe Dashboard", layout="wide")
    st.title("📊 PhonePe Business Intelligence Dashboard")

    # ---------------- DB CONNECTION ----------------
    @st.cache_resource
    def get_connection():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Annusingh123@",
            database="phonepe_db"
        )

    conn = get_connection()

    def run_query(query):
        try:
            return pd.read_sql(query, conn)
        except Exception as e:
            st.error(f"Query Error: {e}")
            return pd.DataFrame()

    
      # ---------------- SCENARIO SELECT ----------------
    scenario = st.sidebar.selectbox("📌 Select Scenario", [
        "Transaction Analysis",
        "User Analysis",
        "Insurance Analysis",
        "Growth Analysis",
        "Top & Bottom Analysis"
    ])
    # ---------------- SIDEBAR FILTERS ----------------
    st.sidebar.header("🔎 Filters")

    year = st.sidebar.selectbox("Select Year", [2018,2019,2020,2021,2022,2023])
    quarter = st.sidebar.selectbox("Select Quarter", [1,2,3,4])
    

    

  


    # 🔹 COMMON FUNCTION (TABLE + PLOT)
    
    def show_chart(df, x, y, chart_type="bar"):
        st.dataframe(df, use_container_width=True)

        if df.empty:
            return

        if chart_type == "bar":
            fig = px.bar(df, x=x, y=y)
        elif chart_type == "line":
            fig = px.line(df, x=x, y=y)
        elif chart_type == "pie":
            fig = px.pie(df, names=x, values=y)
        else:
            fig = px.bar(df, x=x, y=y)

        st.plotly_chart(fig, use_container_width=True)

    
    # SCENARIO 1: TRANSACTION ANALYSIS (5 QUERIES)
   
    if scenario == "Transaction Analysis":
        st.header("💳 Transaction Analysis")

        queries = [
            ("Top States",
            f"""SELECT state, SUM(transaction_amount) total
                FROM aggregated_transaction
                WHERE year={year} AND quarter={quarter}
                GROUP BY state ORDER BY total DESC LIMIT 10""",
            "state","total","bar"),

            ("Transaction Type Share",
            f"""SELECT transaction_type, SUM(transaction_amount) total
                FROM aggregated_transaction
                WHERE year={year} AND quarter={quarter}
                GROUP BY transaction_type""",
            "transaction_type","total","pie"),

            ("Top Districts",
            f"""SELECT district, SUM(transaction_amount) total
                FROM top_transaction_district
                WHERE year={year} AND quarter={quarter}
                GROUP BY district ORDER BY total DESC LIMIT 10""",
            "district","total","bar"),

            ("Top Pincodes",
            f"""SELECT pincode, SUM(transaction_amount) total
                FROM top_transaction_pincode
                WHERE year={year} AND quarter={quarter}
                GROUP BY pincode ORDER BY total DESC LIMIT 10""",
            "pincode","total","bar"),

            ("Yearly Growth",
            """SELECT year, SUM(transaction_amount) total
                FROM aggregated_transaction
                GROUP BY year ORDER BY year""",
            "year","total","line"),
        ]

    #  SCENARIO 2: USER ANALYSIS (5 QUERIES)
   
    elif scenario == "User Analysis":
        st.header("👥 User Analysis")

        queries = [
            ("Users by State",
            f"""SELECT state, SUM(user_count) users
                FROM aggregated_user
                WHERE year={year} AND quarter={quarter}
                GROUP BY state ORDER BY users DESC""",
            "state","users","bar"),

            ("Brand Usage",
            f"""SELECT brand, SUM(user_count) users
                FROM aggregated_user
                WHERE year={year} AND quarter={quarter}
                GROUP BY brand""",
            "brand","users","pie"),

            ("Top District Users",
            f"""SELECT district, SUM(registered_users) users
                FROM map_user
                WHERE year={year} AND quarter={quarter}
                GROUP BY district ORDER BY users DESC LIMIT 10""",
            "district","users","bar"),

            ("App Opens",
            f"""SELECT state, SUM(app_opens) opens
                FROM map_user
                WHERE year={year} AND quarter={quarter}
                GROUP BY state ORDER BY opens DESC""",
            "state","opens","bar"),

            ("Engagement Ratio",
            f"""SELECT state,
            SUM(app_opens) / NULLIF(SUM(registered_users), 0) AS engagement
            FROM map_user
            WHERE year = {year} AND quarter = {quarter}
            GROUP BY state
            ORDER BY engagement DESC""",
            "state","engagement","bar")
        ]

    
    #  SCENARIO 3: INSURANCE ANALYSIS (5 QUERIES)
    
    elif scenario == "Insurance Analysis":
        st.header("🛡️ Insurance Analysis")

        queries = [
            ("Insurance by State",
            f"""SELECT state, SUM(transaction_amount) total
                FROM aggregated_insurance
                WHERE year={year} AND quarter={quarter}
                GROUP BY state ORDER BY total DESC""",
            "state","total","bar"),

            ("Top District Insurance",
            f"""SELECT district, SUM(insurance_amount) total
                FROM top_insurance_district
                WHERE year={year} AND quarter={quarter}
                GROUP BY district ORDER BY total DESC LIMIT 10""",
            "district","total","bar"),

            ("Top Pincode Insurance",
            f"""SELECT pincode, SUM(insurance_amount) total
                FROM top_insurance_pincode
                WHERE year={year} AND quarter={quarter}
                GROUP BY pincode ORDER BY total DESC LIMIT 10""",
            "pincode","total","bar"),

            ("Insurance Growth",
            """SELECT year, SUM(transaction_amount) total
                FROM aggregated_insurance
                GROUP BY year""",
            "year","total","line"),

            ("Insurance Share",
            f"""SELECT state, SUM(transaction_amount) total
                FROM aggregated_insurance
                WHERE year={year}
                GROUP BY state""",
            "state","total","pie"),
        ]

    
    #  SCENARIO 4: GROWTH ANALYSIS (5 QUERIES)
  
    elif scenario == "Growth Analysis":
        st.header("📈 Growth Analysis")

        queries = [
            ("Yearly Growth","""SELECT year, SUM(user_count) users 
                FROM aggregated_user 
                GROUP BY year""",
                "year","users","line"),
            ("Quarterly Growth",
                f"""SELECT quarter, SUM(user_count) users 
                    FROM aggregated_user 
                    WHERE year={year}
                    GROUP BY quarter
                    ORDER BY quarter""",
                "quarter","users","line"),

            ("Transaction Growth",
            "SELECT year, SUM(transaction_amount) total FROM aggregated_transaction GROUP BY year",
            "year","total","line"),

            ("App Opens Growth",
            "SELECT year, SUM(app_opens) opens FROM map_user GROUP BY year",
            "year","opens","line"),

            ("Top States Growth",
            f"""SELECT state, SUM(transaction_amount) total
                FROM aggregated_transaction
                WHERE year={year}
                GROUP BY state ORDER BY total DESC LIMIT 10""",
            "state","total","bar"),

            ("User Distribution",
            "SELECT state, SUM(user_count) users FROM aggregated_user GROUP BY state LIMIT 10",
            "state","users","bar"),
        ]

    
    #  SCENARIO 5: TOP & BOTTOM ANALYSIS (5 QUERIES)

    elif scenario == "Top & Bottom Analysis":
        st.header("🏆 Top & Bottom Analysis")

        queries = [
            ("Top States",
            "SELECT state, SUM(transaction_amount) total FROM aggregated_transaction GROUP BY state ORDER BY total DESC LIMIT 10",
            "state","total","bar"),

            ("Low States",
            "SELECT state, SUM(transaction_amount) total FROM aggregated_transaction GROUP BY state ORDER BY total ASC LIMIT 10",
            "state","total","bar"),

            ("Low Districts",
            f"""SELECT district, SUM(transaction_amount) total
                FROM map_transaction_district
                WHERE year={year} AND quarter={quarter}
                GROUP BY district ORDER BY total ASC LIMIT 10""",
            "district","total","bar"),

            ("State Contribution",
            f"""SELECT state, SUM(transaction_amount) total
                FROM map_transaction_state
                WHERE year={year} AND quarter={quarter}
                GROUP BY state""",
            "state","total","pie"),

            ("Top Combined Areas",
            f"""SELECT state, district, SUM(transaction_amount) total
                FROM map_transaction_combined
                WHERE year={year} AND quarter={quarter}
                GROUP BY state, district
                ORDER BY total DESC LIMIT 10""",
            "district","total","bar"),
        ]


    #  EXECUTE QUERIES LOOP (CLEAN UI)
 
    for title, query, x, y, chart in queries:
        st.subheader(title)
        df = run_query(query)
        show_chart(df, x, y, chart)
        st.markdown("---")