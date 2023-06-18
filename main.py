'main file'
import reshape_data.reshape_data as rs


if __name__ == '__main__':

    # Apply the duration_in_days function to the 'date_of_birth' column
    preprocessed_df = rs.apply_function_to_series('test_file',
                                                  'date_of_birth',
                                                  'duration',
                                                  rs.duration_in_days)

    # Print the modified DataFrame
    print(preprocessed_df)
