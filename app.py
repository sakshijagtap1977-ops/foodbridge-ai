
import streamlit as st

st.set_page_config(page_title="FoodBridge AI", page_icon="🍱")

st.title("🍱 FoodBridge AI")
st.write("Connecting surplus food with people in need.")

if "donations" not in st.session_state:
    st.session_state.donations = []

page = st.sidebar.selectbox(
    "Choose Option",
    ["Add Donation", "Find Food"]
)

if page == "Add Donation":
    st.header("Donate Food")

    donor = st.text_input("Your Name")
    food = st.text_input("Food Name")

    category = st.selectbox(
        "Food Category",
        ["Cooked Food", "Fruits", "Vegetables",
         "Bakery", "Packaged Food", "Other"]
    )

    quantity = st.text_input("Quantity")
    location = st.text_input("Your Location")

    if st.button("Submit Donation"):
        if donor.strip() and food.strip() and quantity.strip() and location.strip():
            st.session_state.donations.append({
                "donor": donor,
                "food": food,
                "category": category,
                "quantity": quantity,
                "location": location
            })
            st.success("Donation added successfully!")
        else:
            st.warning("Please fill in all fields.")

elif page == "Find Food":
    st.header("Find Available Food")

    search_location = st.text_input("Preferred Location")

    search_category = st.selectbox(
        "Choose Food Category",
        ["All", "Cooked Food", "Fruits",
         "Vegetables", "Bakery", "Packaged Food", "Other"]
    )

    matches = [
        item for item in st.session_state.donations
        if search_location.strip().lower() in item["location"].lower()
        and (
            search_category == "All"
            or item["category"] == search_category
        )
    ]

    if st.button("Search Food"):
        if matches:
            for item in matches:
                st.subheader(item["food"])
                st.write("Quantity:", item["quantity"])
                st.write("Location:", item["location"])
                st.write("Donor:", item["donor"])

                if st.button("Request Food", key=item["food"] + item["donor"]):
                    st.info("Contact the donor to confirm your request.")
        else:
            st.info("No matching donations found. Try another choice.")
