import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="CineMax Movie Booking",
    page_icon="🎬",
    layout="wide"
)

# Initialize session state for movies
if 'movies' not in st.session_state:
    st.session_state.movies = [
        {"name": "Devara: Part 1", "price": 280, "rating": "UA", "seats": 60},
        {"name": "Pushpa 2: The Rule", "price": 300, "rating": "UA", "seats": 50},
        {"name": "Game Changer", "price": 270, "rating": "U", "seats": 45},
        {"name": "Kalki 2898 AD", "price": 350, "rating": "UA", "seats": 40},
        {"name": "Hanuman", "price": 250, "rating": "U", "seats": 55},
        {"name": "Jailer", "price": 280, "rating": "UA", "seats": 50},
        {"name": "Salaar", "price": 320, "rating": "A", "seats": 35},
        {"name": "RRR", "price": 300, "rating": "UA", "seats": 60},
        {"name": "Arjun Reddy", "price": 260, "rating": "A", "seats": 30},
        {"name": "Bahubali 2", "price": 280, "rating": "U", "seats": 80},
        {"name": "Hi Nanna", "price": 260, "rating": "U", "seats": 50},
        {"name": "Dasara", "price": 280, "rating": "UA", "seats": 45},
        {"name": "Jersey", "price": 250, "rating": "U", "seats": 40},
        {"name": "Shyam Singha Roy", "price": 270, "rating": "UA", "seats": 35},
        {"name": "Ninnu Kori", "price": 240, "rating": "U", "seats": 55},
        {"name": "MCA (Middle Class Abbayi)", "price": 250, "rating": "UA", "seats": 50}
    ]

if 'booking_history' not in st.session_state:
    st.session_state.booking_history = []

# Functions
def calculate_bill(price, tickets):
    """Calculate subtotal, GST, and total amount"""
    subtotal = price * tickets
    gst = subtotal * 0.05
    total = subtotal + gst
    return subtotal, gst, total

def get_movie_dataframe():
    """Convert movies list to pandas DataFrame"""
    df = pd.DataFrame(st.session_state.movies)
    df.index = df.index + 1
    df.columns = ['Movie Name', 'Price (₹)', 'Rating', 'Seats Available']
    return df

def get_rating_info(rating):
    """Get rating information with emoji"""
    if rating == "U":
        return "🟢 U (Universal)"
    elif rating == "UA":
        return "🟡 UA (Parental Guidance)"
    else:
        return "🔴 A (Adults Only 18+)"

def show_movie_details(movie):
    """Display movie details in a container"""
    st.subheader(f"🎥 {movie['name']}")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("💰 Price", f"₹{movie['price']}")
    with col2:
        st.metric("💺 Seats Available", movie['seats'])
    with col3:
        st.write(f"**📊 Rating:** {get_rating_info(movie['rating'])}")

def display_booking_summary(movie, tickets, subtotal, gst, total):
    """Display booking confirmation summary"""
    st.success("✅ BOOKING SUCCESSFUL!")
    st.write("---")
    st.subheader("🎉 Booking Confirmation")
    st.write(f"**🎬 Movie:** {movie['name']}")
    st.write(f"**🎟️ Tickets Booked:** {tickets}")
    st.write(f"**💰 Subtotal:** ₹{subtotal:.2f}")
    st.write(f"**🧾 GST (5%):** ₹{gst:.2f}")
    st.write("---")
    st.subheader(f"💵 Total Amount: ₹{total:.2f}")
    st.write("---")
    st.write(f"**💺 Remaining Seats:** {movie['seats']}")
    st.write("")
    st.write("### 🍿 Enjoy your movie! 🎬")

# ========== HEADER ==========
st.title("🎟️ CINEMAX MOVIE BOOKING SYSTEM")
st.header("🍿 Book Your Favorite Telugu Movies Now!")
st.write("---")

# ========== SIDEBAR ==========
with st.sidebar:
    st.title("📋 BOOKING HISTORY")
    st.write("---")
    
    if st.session_state.booking_history:
        for i, booking in enumerate(st.session_state.booking_history, 1):
            with st.container():
                st.subheader(f"Booking #{i}")
                st.write(f"🎬 **Movie:** {booking['movie']}")
                st.write(f"🎟️ **Tickets:** {booking['tickets']}")
                st.write(f"💵 **Amount:** ₹{booking['total']:.2f}")
                st.write("---")
    else:
        st.info("📝 No bookings yet! Start booking now!")
    
    st.write("")
    st.write("")
    
    if st.button("🔄 RESET ALL SEATS", use_container_width=True):
        st.session_state.movies = [
            {"name": "Devara: Part 1", "price": 280, "rating": "UA", "seats": 60},
            {"name": "Pushpa 2: The Rule", "price": 300, "rating": "UA", "seats": 50},
            {"name": "Game Changer", "price": 270, "rating": "U", "seats": 45},
            {"name": "Kalki 2898 AD", "price": 350, "rating": "UA", "seats": 40},
            {"name": "Hanuman", "price": 250, "rating": "U", "seats": 55},
            {"name": "Jailer", "price": 280, "rating": "UA", "seats": 50},
            {"name": "Salaar", "price": 320, "rating": "A", "seats": 35},
            {"name": "RRR", "price": 300, "rating": "UA", "seats": 60},
            {"name": "Arjun Reddy", "price": 260, "rating": "A", "seats": 30},
            {"name": "Bahubali 2", "price": 280, "rating": "U", "seats": 80},
            {"name": "Hi Nanna", "price": 260, "rating": "U", "seats": 50},
            {"name": "Dasara", "price": 280, "rating": "UA", "seats": 45},
            {"name": "Jersey", "price": 250, "rating": "U", "seats": 40},
            {"name": "Shyam Singha Roy", "price": 270, "rating": "UA", "seats": 35},
            {"name": "Ninnu Kori", "price": 240, "rating": "U", "seats": 55},
            {"name": "MCA (Middle Class Abbayi)", "price": 250, "rating": "UA", "seats": 50}
        ]
        st.session_state.booking_history = []
        st.success("✅ All seats have been reset successfully!")
        st.rerun()

# ========== MAIN TABS ==========
tab1, tab2 = st.tabs(["🎬 BOOK TICKETS", "📊 ALL MOVIES LIST"])

# ========== TAB 2: ALL MOVIES LIST ==========
with tab2:
    st.header("📽️ ALL AVAILABLE MOVIES")
    st.write("---")
    
    # Get and display dataframe
    df = get_movie_dataframe()
    st.dataframe(df, use_container_width=True, height=600)
    
    st.write("---")
    st.header("📈 SUMMARY STATISTICS")
    st.write("")
    
    # Calculate statistics
    total_movies = len(st.session_state.movies)
    total_seats = sum(movie['seats'] for movie in st.session_state.movies)
    avg_price = sum(movie['price'] for movie in st.session_state.movies) / len(st.session_state.movies)
    available_movies = len([m for m in st.session_state.movies if m['seats'] > 0])
    
    # Display statistics in columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("TOTAL MOVIES", total_movies, delta=None)
    
    with col2:
        st.metric("TOTAL SEATS", total_seats, delta=None)
    
    with col3:
        st.metric("AVERAGE PRICE", f"₹{avg_price:.0f}", delta=None)
    
    with col4:
        st.metric("AVAILABLE", available_movies, delta=None)
    
    st.write("---")
    
    # Show movies by rating
    st.subheader("🎬 Movies by Rating")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**🟢 U Rated Movies**")
        u_movies = [m for m in st.session_state.movies if m['rating'] == 'U']
        for movie in u_movies:
            st.write(f"• {movie['name']}")
    
    with col2:
        st.write("**🟡 UA Rated Movies**")
        ua_movies = [m for m in st.session_state.movies if m['rating'] == 'UA']
        for movie in ua_movies:
            st.write(f"• {movie['name']}")
    
    with col3:
        st.write("**🔴 A Rated Movies**")
        a_movies = [m for m in st.session_state.movies if m['rating'] == 'A']
        for movie in a_movies:
            st.write(f"• {movie['name']}")

# ========== TAB 1: BOOK TICKETS ==========
with tab1:
    col1, col2 = st.columns([2, 1])
    
    # Left Column - Booking Form
    with col1:
        st.header("🎬 SELECT YOUR MOVIE")
        st.write("---")
        
        # Movie selection dropdown
        movie_names = [movie['name'] for movie in st.session_state.movies]
        selected_movie_name = st.selectbox(
            "🎥 Choose a movie:",
            movie_names,
            help="Select the movie you want to watch"
        )
        
        # Get selected movie details
        selected_movie = next(movie for movie in st.session_state.movies if movie['name'] == selected_movie_name)
        
        st.write("")
        
        # Display movie details
        with st.container():
            show_movie_details(selected_movie)
        
        st.write("")
        
        # Show warnings based on seat availability
        if selected_movie['seats'] == 0:
            st.error("❌ HOUSEFULL! NO SEATS AVAILABLE FOR THIS MOVIE!")
        elif selected_movie['seats'] < 10:
            st.warning(f"⚠️ HURRY! ONLY {selected_movie['seats']} SEATS LEFT!")
        
        st.write("")
        
        # Ticket count input
        tickets = st.number_input(
            "🎟️ Number of Tickets (Maximum 6):",
            min_value=1,
            max_value=6,
            value=1,
            step=1,
            help="You can book maximum 6 tickets per transaction"
        )
        
        st.write("")
        
        # Age verification for A-rated movies
        age_verified = True
        if selected_movie['rating'] == "A":
            st.warning("🔞 THIS IS AN A-RATED MOVIE. AGE VERIFICATION REQUIRED!")
            age = st.number_input(
                "Enter your age:",
                min_value=1,
                max_value=100,
                value=18,
                step=1
            )
            if age < 18:
                st.error("🚫 YOU MUST BE 18+ TO WATCH THIS MOVIE!")
                age_verified = False
        
        st.write("")
        st.write("")
        
        # Booking button
        if st.button("🎫 BOOK TICKETS NOW", type="primary", use_container_width=True):
            # Validation checks
            if selected_movie['seats'] == 0:
                st.error("❌ SORRY! THIS SHOW IS HOUSEFULL. PLEASE SELECT ANOTHER MOVIE.")
            
            elif not age_verified:
                st.error("❌ AGE VERIFICATION FAILED! YOU MUST BE 18+ TO BOOK THIS MOVIE.")
            
            elif tickets > selected_movie['seats']:
                st.error(f"⚠️ ONLY {selected_movie['seats']} SEATS AVAILABLE. PLEASE SELECT FEWER TICKETS.")
            
            else:
                # Calculate bill
                subtotal, gst, total = calculate_bill(selected_movie['price'], tickets)
                
                # Update seats
                selected_movie['seats'] -= tickets
                
                # Add to booking history
                st.session_state.booking_history.append({
                    'movie': selected_movie['name'],
                    'tickets': tickets,
                    'total': total
                })
                
                st.write("")
                
                # Display booking summary
                display_booking_summary(selected_movie, tickets, subtotal, gst, total)
                
                # Show balloons animation
                st.balloons()
    
    # Right Column - Quick Stats
    with col2:
        st.header("📊 QUICK STATS")
        st.write("---")
        
        # Calculate stats
        total_movies = len(st.session_state.movies)
        total_bookings = len(st.session_state.booking_history)
        total_revenue = sum(booking['total'] for booking in st.session_state.booking_history)
        total_tickets_sold = sum(booking['tickets'] for booking in st.session_state.booking_history)
        
        # Display stats
        st.metric("Total Movies", total_movies)
        st.write("")
        
        st.metric("Total Bookings", total_bookings)
        st.write("")
        
        st.metric("Tickets Sold", total_tickets_sold)
        st.write("")
        
        st.metric("Total Revenue", f"₹{total_revenue:.2f}")
        
        st.write("---")
        
        # Premium movies section
        st.subheader("🔥 PREMIUM MOVIES")
        st.write("")
        
        featured = sorted(st.session_state.movies, key=lambda x: x['price'], reverse=True)[:5]
        
        for i, movie in enumerate(featured, 1):
            with st.container():
                st.write(f"**{i}. {movie['name']}**")
                st.write(f"💰 ₹{movie['price']} | 💺 {movie['seats']} seats")
                st.write("")

# ========== FOOTER ==========
st.write("---")
st.write("")
st.header("🎬 CINEMAX - YOUR ULTIMATE MOVIE BOOKING EXPERIENCE")
st.write("Powered by Streamlit | © 2024 | All Rights Reserved")
st.write("📞 Contact: +91 1234567890 | 📧 support@cinemax.com")
st.write("")