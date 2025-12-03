
import streamlit as st
import pandas as pd
import plotly.express as px
import io
import json
from fpdf import FPDF

# Placeholder for google.generativeai - actual implementation would connect to the API

# --- Helper classes (mimicking TypeScript interfaces for type hinting) ---

class Product:
    def __init__(self, id, name, purchasePrice, sellingPrice, unitsSoldWeek, category=None, stockLevel=None, supplier=None):
        self.id = id
        self.name = name
        self.purchasePrice = purchasePrice
        self.sellingPrice = sellingPrice
        self.unitsSoldWeek = unitsSoldWeek
        self.category = category
        self.stockLevel = stockLevel
        self.supplier = supplier

class CalculatedProduct(Product):
    def __init__(self, id, name, purchasePrice, sellingPrice, unitsSoldWeek, weeklyProfit, margin, weeklyRevenue, category=None, stockLevel=None, supplier=None):
        super().__init__(id, name, purchasePrice, sellingPrice, unitsSoldWeek, category, stockLevel, supplier)
        self.weeklyProfit = weeklyProfit
        self.margin = margin
        self.weeklyRevenue = weeklyRevenue


# --- Helper functions (to be developed/translated from .ts files) ---

def calculate_product_metrics(df):
    if df is not None and not df.empty:
        df['weeklyProfit'] = (df['sellingPrice'] - df['purchasePrice']) * df['unitsSoldWeek']
        df['margin'] = ((df['sellingPrice'] - df['purchasePrice']) / df['sellingPrice']) * 100
        df['weeklyRevenue'] = df['sellingPrice'] * df['unitsSoldWeek']
    return df


def get_ai_insight(products_data, question):
    st.info(f"AI Insight request for: '{question}' with {len(products_data)} products.")
    # In a real app, this would call the Gemini API in Python
    # For now, it's a placeholder response
    return {"insight": "This is a placeholder AI insight based on your question.", "visualization": None}

def generate_compliance_checklist(location, business_type):
    st.info(f"Generating compliance checklist for {business_type} in {location}.")
    return [{"task": "Placeholder Task 1", "details": "Details for task 1"}, {"task": "Placeholder Task 2", "details": "Details for task 2"}]

def get_marketing_advice(product, discount, lift, new_price, simulated_profit):
    st.info(f"Generating marketing advice for {product.name}.")
    return {"advice": "Placeholder marketing advice.", "visualization": None}

def parse_unstructured_data(file_content):
    st.info("Parsing unstructured data with AI.")
    try:
        df_parsed = pd.read_csv(io.StringIO(file_content))
        if all(col in df_parsed.columns for col in ['name', 'sellingPrice', 'purchasePrice', 'unitsSoldWeek']):
            products = []
            for _, row in df_parsed.iterrows():
                products.append({
                    "name": row.get('name', 'Unknown'),
                    "purchasePrice": float(row.get('purchasePrice', 0)),
                    "sellingPrice": float(row.get('sellingPrice', 0)),
                    "unitsSoldWeek": int(row.get('unitsSoldWeek', 0))
                })
            return products
        else:
            st.warning("Uploaded data does not contain expected columns: name, sellingPrice, purchasePrice, unitsSoldWeek. Using placeholder.")
            return []
    except Exception as e:
        st.warning(f"Could not parse unstructured data as CSV: {e}. Using placeholder.")
        return []

def get_sales_forecast_and_suggestions(products_data):
    st.info("Generating sales forecast and suggestions.")
    forecasted_products = []
    for p in products_data:
        forecasted_sales = p.unitsSoldWeek * 1.05
        stock = p.stockLevel if p.stockLevel is not None else 0
        reorder_amount = max(0, forecasted_sales - stock)
        reorder_suggestion = f"Reorder {int(reorder_amount)}" if reorder_amount > 0 else "Sufficient Stock"
        if stock > forecasted_sales * 2:
            reorder_suggestion = "Potentially Overstocked"

        forecasted_products.append({
            **p.__dict__, # Convert CalculatedProduct to dict
            "forecastedSales": forecasted_sales,
            "reorderSuggestion": reorder_suggestion
        })
    return forecasted_products

def generate_full_pdf_report_content(metrics, products_data):
    st.info("Generating full PDF report content.")
    report_content = {
        "reportTitle": "MSPCC Audit Report",
        "reportDate": pd.Timestamp.now().strftime('%Y-%m-%d'),
        "executiveSummary": {
            "overview": "This is a placeholder executive summary. Overall business performance is fair.",
            "keyMetrics": [
                {"label": "Total Weekly Profit", "value": f"${metrics['totalWeeklyProfit']:.2f}", "status": "Neutral"},
                {"label": "Total Weekly Revenue", "value": f"${metrics['totalWeeklyRevenue']:.2f}", "status": "Neutral"},
            ]
        },
        "dataQuality": {
            "summary": "Placeholder data quality summary. Data seems generally good.",
            "score": "Good",
            "checks": []
        },
        "categoryAnalysis": [],
        "marketAnalysis": {
            "topPerformers": ["Product A"],
            "underPerformers": ["Product X"],
            "opportunityGaps": ["Expand into new categories"]
        },
        "strategicRecommendations": [],
        "conclusion": "Placeholder conclusion."
    }
    return report_content

def generate_business_overview_stream(metrics, products_data):
    st.info("Generating business overview stream.")
    yield "### Business Overview"
    yield f"Current total weekly profit: **${metrics['totalWeeklyProfit']:.2f}**
    yield "No critical alerts at this time."

def extract_web_data(products_data, query):
    st.info(f"Extracting web data for query: '{query}'")
    return {
        "headers": ["Item", "Price", "Source"],
        "data": [
            ["Example Item 1", 10.99, "Simulated Website A"],
            ["Example Item 2", 24.50, "Simulated Website B"]
        ]
    }


# FPDF Report Generation (translation from reportGenerator.ts)
def generate_pdf_report(report_content, metrics, products):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=report_content["reportTitle"], ln=True, align='C')
    pdf.cell(200, 10, txt=f"Report Date: {report_content['reportDate']}", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", 'B', size=14)
    pdf.cell(200, 10, txt="Executive Summary", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 5, report_content["executiveSummary"]["overview"])
    pdf.ln(5)

    for metric in report_content["executiveSummary"]["keyMetrics"]:
        pdf.cell(0, 5, txt=f"{metric['label']}: {metric['value']} ({metric['status']})", ln=True)
    pdf.ln(10)

    pdf.set_font("Arial", 'B', size=14)
    pdf.cell(200, 10, txt="Detailed Product Data (Sample)", ln=True)
    pdf.set_font("Arial", size=10)
    
    headers = ["Name", "Selling Price", "Weekly Profit"]
    data = []
    for p in products[:5]:
        data.append([p.name, f"${p.sellingPrice:.2f}", f"${p.weeklyProfit:.2f}"])

    col_widths = [60, 40, 40]
    
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 7, header, 1, 0, 'C')
    pdf.ln()

    for row in data:
        for i, item in enumerate(row):
            pdf.cell(col_widths[i], 7, item, 1, 0, 'C')
        pdf.ln()
    
    pdf_output = pdf.output(dest='S').encode('latin-1')
    return io.BytesIO(pdf_output)


# --- Streamlit UI ---

st.set_page_config(layout="wide", page_title="MSPCC Analytical Dashboard")

# Initialize session state for product data
if 'products_df' not in st.session_state:
    st.session_state.products_df = pd.DataFrame(columns=[
        'id', 'name', 'purchasePrice', 'sellingPrice', 'unitsSoldWeek',
        'category', 'stockLevel', 'supplier', 'weeklyProfit', 'margin', 'weeklyRevenue'
    ])
    st.session_state.next_product_id = 1

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Data Upload", "AI Insights", "Marketing Simulator", "Sales Forecast", "Compliance Checklist", "Web Data Extractor", "Report Generator"])


if page == "Dashboard":
    st.title("📊 Analytical Dashboard")
    st.markdown("Welcome to your MSPCC Analytical Dashboard. Gain insights into your product performance.")

    if not st.session_state.products_df.empty:
        total_profit = st.session_state.products_df['weeklyProfit'].sum()
        total_revenue = st.session_state.products_df['weeklyRevenue'].sum()
        avg_margin = st.session_state.products_df['margin'].mean() if not st.session_state.products_df.empty else 0

        metrics_data = {
            'totalWeeklyProfit': total_profit,
            'totalWeeklyRevenue': total_revenue,
            'averageMargin': avg_margin
        }

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Weekly Profit", f"${total_profit:,.2f}")
        with col2:
            st.metric("Total Weekly Revenue", f"${total_revenue:,.2f}")
        with col3:
            st.metric("Average Margin", f"{avg_margin:.1f}%")

        st.subheader("Product Performance Overview")
        st.dataframe(st.session_state.products_df[['name', 'category', 'sellingPrice', 'unitsSoldWeek', 'weeklyProfit', 'margin']].head(10), use_container_width=True)

        st.subheader("Profitability Charts")
        fig = px.bar(st.session_state.products_df.sort_values('weeklyProfit', ascending=False).head(10),
                     x='name', y='weeklyProfit', title='Top 10 Products by Weekly Profit')
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Live Business Overview (AI)")
        overview_metrics = {
            'totalWeeklyProfit': total_profit,
        }
        products_for_ai = [
            CalculatedProduct(
                id=row['id'],
                name=row['name'],
                purchasePrice=row['purchasePrice'],
                sellingPrice=row['sellingPrice'],
                unitsSoldWeek=row['unitsSoldWeek'],
                weeklyProfit=row['weeklyProfit'],
                margin=row['margin'],
                weeklyRevenue=row['weeklyRevenue'],
                category=row.get('category'),
                stockLevel=row.get('stockLevel'),
                supplier=row.get('supplier')
            )
            for _, row in st.session_state.products_df.iterrows()
        ]
        
        overview_generator = generate_business_overview_stream(overview_metrics, products_for_ai)
        overview_text = st.empty()
        full_overview = ""
        for chunk in overview_generator:
            full_overview += chunk
            overview_text.markdown(full_overview)
    else:
        st.info("Please upload product data via the 'Data Upload' page to see dashboard insights.")

elif page == "Data Upload":
    st.title("⬆️ Upload Product Data")
    st.markdown("Upload your product data in a CSV or text format. The AI will attempt to parse it.")

    uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt"])

    if uploaded_file is not None:
        file_content = uploaded_file.getvalue().decode("utf-8")
        st.text_area("File Content Preview", file_content, height=200)

        if st.button("Process Data with AI"):
            with st.spinner("Parsing data and calculating metrics..."):
                parsed_products_list = parse_unstructured_data(file_content)

                if parsed_products_list:
                    new_products_df = pd.DataFrame(parsed_products_list)
                    
                    current_id = st.session_state.next_product_id
                    new_products_df['id'] = range(current_id, current_id + len(new_products_df))
                    st.session_state.next_product_id += len(new_products_df)

                    new_products_df = calculate_product_metrics(new_products_df)
                    
                    st.session_state.products_df = pd.concat([st.session_state.products_df, new_products_df], ignore_index=True)
                    st.success("Data processed and added to dashboard!")
                    st.dataframe(new_products_df) # Show newly added data
                else:
                    st.error("AI could not extract valid product data from the file. Please check format.")
    
    st.subheader("Current Loaded Data Sample")
    if not st.session_state.products_df.empty:
        st.dataframe(st.session_state.products_df.head())
    else:
        st.info("No product data loaded yet.")


elif page == "AI Insights":
    st.title("💡 AI-Powered Business Insights")
    st.markdown("Ask a question about your product data and get AI-driven insights and visualizations.")

    if not st.session_state.products_df.empty:
        question = st.text_area("What would you like to know about your products?", "What are my most profitable products and why?")

        if st.button("Get Insight"):
            with st.spinner("Generating AI insight..."):
                products_for_ai = [
                    CalculatedProduct(
                        id=row['id'],
                        name=row['name'],
                        purchasePrice=row['purchasePrice'],
                        sellingPrice=row['sellingPrice'],
                        unitsSoldWeek=row['unitsSoldWeek'],
                        weeklyProfit=row['weeklyProfit'],
                        margin=row['margin'],
                        weeklyRevenue=row['weeklyRevenue'],
                        category=row.get('category'),
                        stockLevel=row.get('stockLevel'),
                        supplier=row.get('supplier')
                    )
                    for _, row in st.session_state.products_df.iterrows()
                ]
                insight_response = get_ai_insight(products_for_ai, question)
                st.subheader("AI Insight")
                st.markdown(insight_response["insight"])
                if insight_response["visualization"]:
                    st.subheader("Visualization")
                    st.json(insight_response["visualization"]) # Display raw JSON for now
                else:
                    st.info("No specific visualization generated for this insight.")
    else:
        st.info("Please upload product data to use AI Insights.")

elif page == "Marketing Simulator":
    st.title("📈 Marketing Promotion Simulator")
    st.markdown("Simulate the impact of price changes and sales lift on product profitability.")

    if not st.session_state.products_df.empty:
        selected_product_name = st.selectbox("Select a Product", st.session_state.products_df['name'].unique())
        
        if selected_product_name:
            selected_product_row = st.session_state.products_df[st.session_state.products_df['name'] == selected_product_name].iloc[0]
            
            current_product = Product(
                id=selected_product_row['id'],
                name=selected_product_row['name'],
                purchasePrice=selected_product_row['purchasePrice'],
                sellingPrice=selected_product_row['sellingPrice'],
                unitsSoldWeek=selected_product_row['unitsSoldWeek']
            )

            st.write(f"**Current Price:** ${current_product.sellingPrice:.2f}")
            st.write(f"**Current Weekly Units Sold:** {current_product.unitsSoldWeek}")
            
            col1, col2 = st.columns(2)
            with col1:
                discount_percent = st.slider("Discount (%)", 0, 50, 10)
                lift_percent = st.slider("Estimated Sales Lift (%)", 0, 200, 20)
            
            new_price = current_product.sellingPrice * (1 - discount_percent / 100)
            simulated_units = current_product.unitsSoldWeek * (1 + lift_percent / 100)
            simulated_profit = (new_price - current_product.purchasePrice) * simulated_units

            st.write(f"**Simulated New Price:** ${new_price:.2f}")
            st.write(f"**Simulated Weekly Units Sold:** {simulated_units:.0f}")
            st.write(f"**Simulated Weekly Profit:** ${simulated_profit:.2f}")

            if st.button("Get Marketing Advice"):
                with st.spinner("Generating marketing advice..."):
                    marketing_response = get_marketing_advice(current_product, discount_percent, lift_percent, new_price, simulated_profit)
                    st.subheader("AI Marketing Advice")
                    st.markdown(marketing_response["advice"])
                    if marketing_response["visualization"]:
                        st.subheader("Comparison Visualization")
                        st.json(marketing_response["visualization"]) # Display raw JSON for now
    else:
        st.info("Please upload product data to use the Marketing Simulator.")

elif page == "Sales Forecast":
    st.title("🔮 Sales Forecast & Inventory Suggestions")
    st.markdown("Get AI-powered sales forecasts and reorder suggestions for your products.")

    if not st.session_state.products_df.empty:
        if st.button("Generate Forecasts"):
            with st.spinner("Generating sales forecasts..."):
                products_for_ai = [
                    CalculatedProduct(
                        id=row['id'],
                        name=row['name'],
                        purchasePrice=row['purchasePrice'],
                        sellingPrice=row['sellingPrice'],
                        unitsSoldWeek=row['unitsSoldWeek'],
                        weeklyProfit=row['weeklyProfit'],
                        margin=row['margin'],
                        weeklyRevenue=row['weeklyRevenue'],
                        category=row.get('category'),
                        stockLevel=row.get('stockLevel'),
                        supplier=row.get('supplier')
                    )
                    for _, row in st.session_state.products_df.iterrows()
                ]
                forecasted_data = get_sales_forecast_and_suggestions(products_for_ai)
                forecast_df = pd.DataFrame(forecasted_data)
                
                st.subheader("Sales Forecast and Reorder Suggestions")
                st.dataframe(forecast_df[['name', 'unitsSoldWeek', 'stockLevel', 'forecastedSales', 'reorderSuggestion']], use_container_width=True)
    else:
        st.info("Please upload product data to generate sales forecasts.")

elif page == "Compliance Checklist":
    st.title("✅ AI Compliance Checklist")
    st.markdown("Generate a general business compliance checklist based on your location and business type.")

    location = st.text_input("Business Location (e.g., 'California')", "California")
    business_type = st.text_input("Business Type (e.g., 'Retail Store', 'Restaurant')", "Retail Store")

    if st.button("Generate Checklist"):
        with st.spinner("Generating compliance checklist..."):
            checklist = generate_compliance_checklist(location, business_type)
            st.subheader("Compliance Checklist")
            for item in checklist:
                st.checkbox(f"**{item['task']}** - {item['details']}", key=item['task'])

elif page == "Web Data Extractor":
    st.title("🌐 Web Data Extractor")
    st.markdown("Use AI to extract structured data from web content based on your query.")

    if not st.session_state.products_df.empty:
        query = st.text_area("Enter your query (e.g., 'latest prices for laptops from bestbuy.com' or 'compare features of Samsung Galaxy S23 vs iPhone 15')",
                             "latest prices for laptops on amazon.com")
        
        if st.button("Extract Data"):
            with st.spinner("Extracting web data..."):
                products_for_ai = [
                    CalculatedProduct(
                        id=row['id'],
                        name=row['name'],
                        purchasePrice=row['purchasePrice'],
                        sellingPrice=row['sellingPrice'],
                        unitsSoldWeek=row['unitsSoldWeek'],
                        weeklyProfit=row['weeklyProfit'],
                        margin=row['margin'],
                        weeklyRevenue=row['weeklyRevenue'],
                        category=row.get('category'),
                        stockLevel=row.get('stockLevel'),
                        supplier=row.get('supplier')
                    )
                    for _, row in st.session_state.products_df.iterrows()
                ]
                extracted_data = extract_web_data(products_for_ai, query)
                
                if extracted_data and extracted_data['data']:
                    st.subheader("Extracted Data")
                    extracted_df = pd.DataFrame(extracted_data['data'], columns=extracted_data['headers'])
                    st.dataframe(extracted_df, use_container_width=True)
                else:
                    st.info("No data extracted for this query.")
    else:
        st.info("Upload product data to give AI context for web data extraction.")

elif page == "Report Generator":
    st.title("📄 Generate Detailed Report")
    st.markdown("Generate a comprehensive PDF report summarizing your product performance.")

    if not st.session_state.products_df.empty:
        if st.button("Generate PDF Report"):
            with st.spinner("Generating report content..."):
                total_profit = st.session_state.products_df['weeklyProfit'].sum()
                total_revenue = st.session_state.products_df['weeklyRevenue'].sum()
                avg_margin = st.session_state.products_df['margin'].mean() if not st.session_state.products_df.empty else 0

                metrics_for_report = {
                    'totalWeeklyProfit': total_profit,
                    'totalWeeklyRevenue': total_revenue,
                    'averageMargin': avg_margin,
                    'profitTrend': [total_profit * (0.9 + i*0.02) for i in range(7)] # Sample trend
                }
                
                products_for_ai = [
                    CalculatedProduct(
                        id=row['id'],
                        name=row['name'],
                        purchasePrice=row['purchasePrice'],
                        sellingPrice=row['sellingPrice'],
                        unitsSoldWeek=row['unitsSoldWeek'],
                        weeklyProfit=row['weeklyProfit'],
                        margin=row['margin'],
                        weeklyRevenue=row['weeklyRevenue'],
                        category=row.get('category'),
                        stockLevel=row.get('stockLevel'),
                        supplier=row.get('supplier')
                    )
                    for _, row in st.session_state.products_df.iterrows()
                ]

                report_content = generate_full_pdf_report_content(metrics_for_report, products_for_ai)
                
            st.success("Report content generated. Creating PDF...")
            pdf_buffer = generate_pdf_report(report_content, metrics_for_report, products_for_ai)
            
            st.download_button(
                label="Download PDF Report",
                data=pdf_buffer,
                file_name=f"MSPCC_Audit_Report_{pd.Timestamp.now().strftime('%Y-%m-%d')}.pdf",
                mime="application/pdf"
            )
    else:
        st.info("Please upload product data to generate a report.")
