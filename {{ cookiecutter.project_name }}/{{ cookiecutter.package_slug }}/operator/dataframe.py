def tolower(dataframe, column):
    """Convert a dataframe column to lowercase

        Args:
            dataframe (DataFrame): Pandas dataframe to update
            column(string): Name of the column to lower case

        Returns:
            dataframe: Updated dataframe
    """
    dataframe[column] = dataframe[column].str.lower()
    return dataframe


def toupper(dataframe, column):
    """Convert a dataframe column to uppercase

        Args:
            dataframe (DataFrame): Pandas dataframe to update
            column(string): Name of the column to upper case

        Returns:
            dataframe: Updated dataframe
    """
    dataframe[column] = dataframe[column].str.upper()
    return dataframe
