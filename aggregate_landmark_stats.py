import pandas as pd

def aggregate_landmark_stats(input_csv, output_csv):
    """
    Aggregate landmark statistics by video and time, pivoting data to separate stats for each landmark.
    Args:
        input_csv (str): Path to the input CSV file.
        output_csv (str): Path to save the aggregated CSV file.
    """
    # Load the CSV file
    df = pd.read_csv(input_csv)

    # Group by Time (seconds), Video Name, and Landmark, aggregating stats
    grouped = df.groupby(['Time (seconds)', 'Video Name', 'Landmark']).agg({
        'angle_std': 'mean',
        'angle_medium': 'mean',
        'angle_median': 'mean',
        'angle_min': 'mean',
        'angle_max': 'mean',
        'velocity_std': 'mean',
        'velocity_medium': 'mean',
        'velocity_median': 'mean',
        'velocity_min': 'mean',
        'velocity_max': 'mean',
        'acceleration_std': 'mean',
        'acceleration_medium': 'mean',
        'acceleration_median': 'mean',
        'acceleration_min': 'mean',
        'acceleration_max': 'mean',
    }).reset_index()

    # Pivot the data to create separate columns for each landmark's stats
    pivoted = grouped.pivot(index=['Time (seconds)', 'Video Name'], columns='Landmark')
    pivoted.columns = [f"{stat}_{landmark}" for stat, landmark in pivoted.columns]
    pivoted.reset_index(inplace=True)

    # Save the pivoted DataFrame to a new CSV file
    pivoted.to_csv(output_csv, index=False)
    print(f"Aggregated and pivoted data saved to: {output_csv}")

# Example usage
input_csv = "c:\\Users\\asus\\Desktop\\work\\Data\\all_landmarks_data_Processed_combined.csv"
output_csv = "c:\\Users\\asus\\Desktop\\work\\Data\\pivoted_landmark_stats.csv"
aggregate_landmark_stats(input_csv, output_csv)
