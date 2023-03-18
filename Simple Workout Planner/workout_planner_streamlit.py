import streamlit as st
import pandas as pd

# Set up the data
workout_df = pd.DataFrame(columns=['Exercise', 'Sets', 'Reps', 'Weight'])

# Define function to add new exercise to the dataframe
def add_new_exercise(exercise_name, num_sets, num_reps, weight):
    global workout_df
    workout_df = workout_df.append({'Exercise': exercise_name, 'Sets': num_sets, 'Reps': num_reps, 'Weight': weight}, ignore_index=True)

# Set up the Streamlit app
st.title("Workout Planner")

# Add up to 20 exercises for the day, with sets, reps, and weight
for i in range(1, 21):
    exercise_name = st.text_input(f"Enter exercise #{i}:")
    if exercise_name:
        num_sets = st.number_input(f"How many sets for exercise #{i}?", min_value=1, step=1)
        num_reps = st.number_input(f"How many reps for exercise #{i}?", min_value=1, step=1)
        weight = st.number_input(f"What weight for exercise #{i}?", min_value=0, step=1)
        add_new_exercise(exercise_name, num_sets, num_reps, weight)
        st.success(f"Exercise #{i} added!")

# Show the exercises for the day
if not workout_df.empty:
    st.write("Exercises for the day:")
    st.write(workout_df)

# Add a button to export the data as a CSV file
if st.button("Export data as CSV"):
    with st.spinner("Exporting data..."):
        workout_df.to_csv("workout_data.csv", index=False)
    st.success("Data exported successfully!")
