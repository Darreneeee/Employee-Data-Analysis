import pandas as pd
import matplotlib.pyplot as plt


#print(df)

# Q1 - What is the distribution of educational qualifications among employees?

    #how many Bachelors, Masters, PHD
def q1():
    education_dist = df["Education"].value_counts()
    education_dist = education_dist.to_frame("Employees")
    education_dist["Percentage(%)"] = (
        (education_dist["Employees"] / education_dist["Employees"].sum()) * 100
    ).round(1)
    print(education_dist)

    education_dist["Employees"].plot(kind="bar", color="#976ec2")
    plt.title("Educational Qualification Distribution", fontweight="bold")
    plt.grid(axis="y", linestyle="dashed", color="#b4b3b5")
    plt.xlabel("Education Qualification", fontweight="bold")
    plt.ylabel("Number of Employees", fontweight="bold")
    plt.xticks(rotation=0)
    plt.show()


# Q2 - How does the length of service (Joining Year) vary across different cities?
def q2():
    city_df = df[["JoiningYear", "City"]]
    city_df["LengthOfService"] = (
        2025 - city_df["JoiningYear"]
    )
    city_group = city_df.groupby("City")
    city_dist = ((city_group["LengthOfService"].mean()).round(3)).to_frame("Mean LOS")
    print(city_dist)

    city_dist.plot(kind="bar", color="#7cc4e6")
    plt.title("Mean Length of Service & City Distribution", fontweight="bold")
    plt.grid(axis="y", color="#b1b2b3", linestyle="dashed")
    plt.xlabel("Cities", fontweight="bold")
    plt.ylabel("Mean LOS", fontweight="bold")
    plt.xticks(rotation=0)
    plt.ylim(9, 10.5)
    plt.show()


# Q3 - Is there a correlation between Payment Tier and Experience in Current Domain?
    # payment tier vs experience
def q3():
    pay_exp_df = df[["PaymentTier", "ExperienceInCurrentDomain"]]
    pay_group = pay_exp_df.groupby("PaymentTier")
    pay_exp_dist = ((pay_group["ExperienceInCurrentDomain"].mean()).round(3)).to_frame("Mean Experience")
    print(pay_exp_dist)
    



# Q4 - What is the gender distribution within the workforce?
def q4():
    gender_df = df["Gender"]
    gender_dist = (gender_df.value_counts()).to_frame("Num of Employee")
    print(gender_dist)
    
    gender_dist.plot(kind="bar", color="#72acd6", legend=False)
    plt.title("Gender Distribution", fontweight="bold")
    plt.xlabel("Gender", fontweight="bold")
    plt.ylabel("Num of Employees", fontweight="bold")
    plt.grid(axis="y", color="#b1b2b3", linestyle="dashed")
    plt.xticks(rotation=0)
    plt.show()


if __name__ == "__main__":
    df = pd.read_csv("Employee.csv")
    q3()