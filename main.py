import pandas as pd
from matplotlib import pyplot as plt


def find_out_what_cheaper(df):
    # df["manufacturer"].unique()
    # df_mers_bmw = df.loc[
    #     (df["manufacturer"] == "bmw") | (df["manufacturer"] == "mercedes-benz")
    # ]
    # df_mers_bmw = df_mers_bmw.loc[df_mers_bmw["year"] > 2018]
    # df_mers_bmw = (
    #     df_mers_bmw.groupby(by="manufacturer")
    #     .agg({"price": "mean"})
    #     .reset_index(drop=True)
    # )
    # print(df_mers_bmw)  # mercedes-benz дороже

    df_audi_volvo = df.loc[
        (df["manufacturer"] == "audi") | (df["manufacturer"] == "volvo")
    ]
    df_audi_volvo = df_audi_volvo.loc[df_audi_volvo["year"] > 2017]
    df_audi_volvo = (
        df_audi_volvo.groupby(by="manufacturer")
        .agg({"price": "mean"})
        .reset_index(drop=True)
    )
    print(df_audi_volvo)  # audi дороже


def build_scatter_plot(df):
    rows_to_drop = df[
        (df["price"] < df["price"].quantile(0.005))
        | (df["price"] > df["price"].quantile(0.995))
    ].index
    df = df.drop(rows_to_drop)
    plt.scatter(df["price"], df["year"])
    plt.show()


def calculating_cars_engines(df):
    data_types_enginesdf = df["fuel"].value_counts()
    plt.pie(data_types_enginesdf, autopct="%.0f%%")
    plt.legend(df["fuel"].unique())
    plt.show()


def get_descriptive_statistics(df):
    descriptive_statistics = df.describe()

    return descriptive_statistics


def searching_missing_values(df):
    cat_features = []
    numerical_features = []

    for i in df.columns:
        if df[i].isna().sum() > len(df) // 3:
            df = df.drop(i, axis=1)

    for i in df.columns:
        if df[i].dtype.name == "object":
            cat_features += [i]
        elif df[i].dtype.name == "float64" or (df[i].dtype.name == "int64"):
            numerical_features += [i]

    df[numerical_features] = df[numerical_features].fillna(
        df[numerical_features].median(axis=0), axis=0
    )
    df[cat_features] = df[cat_features].fillna(df[cat_features].mode().iloc[0])

    sum_omissions = df.isna().sum()

    return sum_omissions


def get_cars_high_mileage(df):
    # df_second = df[["manufacturer", "model", "odometer"]].loc[df["year"] > 2020]
    # rows_to_drop = df_second[
    #     (df_second["odometer"] < df_second["odometer"].quantile(0.005))
    #     | (df_second["odometer"] > df_second["odometer"].quantile(0.995))
    # ].index
    # df_second = df_second.drop(rows_to_drop)
    # df_second = df_second.sort_values(by="odometer", ascending=False)
    # df_second = df_second.drop_duplicates()
    # df_second = df_second.head(3)
    # print(df_second)

    df_second = df[["manufacturer", "model", "odometer"]].loc[df["year"] > 2018]
    rows_to_drop = df_second[
        (df_second["odometer"] < df_second["odometer"].quantile(0.005))
        | (df_second["odometer"] > df_second["odometer"].quantile(0.995))
    ].index
    df_second = df_second.drop(rows_to_drop)
    df_second = df_second.sort_values(by="odometer")
    df_second = df_second.drop_duplicates()
    df_second = df_second.head(3)
    print(df_second)


def col_mers_very_expensive(df):
    # df_third = df[["manufacturer", "price"]]
    # df_third = df_third.sort_values(by="price", ascending=False)
    # df_third = df_third.head(100)
    # df_third = df_third["manufacturer"].value_counts()["mercedes-benz"]
    # print(df_third)

    df_third = df[["manufacturer", "price"]]
    df_third = df_third.drop_duplicates().reset_index(drop=True)
    df_third = df_third.sort_values(by="price", ascending=False)
    df_top_100 = df_third.head(100)
    car_count = df_top_100["manufacturer"].value_counts().get('audi', 0)
    print(car_count)


def main():
    df = pd.read_csv("vehicles.csv")
    # sum_omissions = searching_missing_values(df)
    # descriptive_statistics = get_descriptive_statistics(df)
    # # calculating_cars_engines(df)
    # build_scatter_plot(df)
    find_out_what_cheaper(df)
    get_cars_high_mileage(df)
    col_mers_very_expensive(df)


if __name__ == "__main__":
    main()
