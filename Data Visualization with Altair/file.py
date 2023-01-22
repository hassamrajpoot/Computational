import matplotlib.pyplot as plt
import pandas as pd
import altair as at

df = pd.read_csv('http://faculty.cs.niu.edu/~dakoop/cs503-2021fa/a8/ny-county-energy.csv.gz', compression='gzip')
total_consumption_df = df[df['data_field_display_name'] == 'Total Consumption (T)']
electricity_df = total_consumption_df[total_consumption_df['data_class'] == 'electricity']
sorted_electricity_df = electricity_df.sort_values('value')
county_name = sorted_electricity_df.iloc[-1]['county_name']
year = sorted_electricity_df.iloc[-1]['year']
month = sorted_electricity_df.iloc[-1]['month']

# 2
sorted_electricity_df_2020 = sorted_electricity_df[sorted_electricity_df['year'] == 2020]
counties = sorted_electricity_df_2020['county_name'].unique().tolist()


def usage_and_number_of_accounts_sums(county):
    county_df = sorted_electricity_df_2020[sorted_electricity_df_2020['county_name'] == county]
    usage_sum = sum(county_df['value'].tolist())
    no_of_accounts_sum = sum(county_df['number_of_accounts'].tolist())
    electricity_per_account = usage_sum / no_of_accounts_sum
    return {'county': county, 'electricity_per_account': electricity_per_account}


data = []


def all_counties_data():
    if not len(counties) == 0:
        data.append(usage_and_number_of_accounts_sums(counties.pop()))
        all_counties_data()
    elif len(counties) == 0:
        return


all_counties_data()
counties_sorted_df = pd.DataFrame(data).sort_values('electricity_per_account')
county_with_highest_electricity_per_account = counties_sorted_df.iloc[-1]['county']


# 2b


def bar_charts(county):
    county_df = total_consumption_df[total_consumption_df['county_name'] == county]
    electric_df = county_df[county_df['data_class'] == 'electricity']
    years = electric_df['year'].unique().tolist()
    years_data = {}
    for current_year in years:
        year_df = electric_df[electricity_df['year'] == current_year]
        years_electricity = sum(year_df['value'].tolist())
        years_data[current_year] = years_electricity
    y = list(years_data.keys())
    values = list(years_data.values())
    plt.bar(y, values)
    plt.title('Electricity')
    plt.xlabel('year')
    plt.ylabel('MWh')
    plt.show()
    natural_gas_df = county_df[county_df['data_class'] == 'natural_gas']
    years_gas_data = {}
    for curr_year in years:
        y_df = natural_gas_df[natural_gas_df['year'] == curr_year]
        years_natural_gas = sum(y_df['value'].tolist())
        years_gas_data[curr_year] = years_natural_gas
    plt.bar(list(years_gas_data.keys()), list(years_gas_data.values()), color='orange')
    plt.title('Natural Gas')
    plt.xlabel('year')
    plt.ylabel('Therms')
    plt.show()
    df_year_and_values_elec = pd.DataFrame({'year': y, 'value': values})
    df_year_and_values_gas = pd.DataFrame({'year': list(years_gas_data.keys()), 'value': list(years_gas_data.values())})
    at.Chart(df_year_and_values_elec, title='Electricity usage by years').mark_bar().encode(x='year:N',
                                                                                            y='value:Q').show()
    at.Chart(df_year_and_values_gas, title='Natural Gas usage by years').mark_bar().encode(x='year:N',
                                                                                           y='value:Q').show()


def line_charts(county):
    county_df = total_consumption_df[total_consumption_df['county_name'] == county]
    electric_df = county_df[county_df['data_class'] == 'electricity']
    years = electric_df['year'].unique().tolist()
    years_data_by_month = []
    for curr_year in years:
        year_df = electric_df[electric_df['year'] == curr_year]
        values = year_df['value'].tolist()
        for v in values:
            years_data_by_month.append(v * 10)
    plt.plot([i for i in range(1, 60 + 1)], years_data_by_month)
    years_list = [2016, 2017, 2018, 2019, 2020]
    plt.xticks(ticks=[1, 12, 24, 36, 48], labels=years_list)
    plt.title('Electricity')
    plt.ylabel('MWh')
    plt.show()
    natural_gas_df = county_df[county_df['data_class'] == 'natural_gas']
    years_data_by_month_natural_gas = []
    for c_year in years:
        y_df = natural_gas_df[natural_gas_df['year'] == c_year]
        vals = y_df['value'].tolist()
        for val in vals:
            years_data_by_month_natural_gas.append(val)
    plt.plot([i for i in range(1, 60 + 1)], years_data_by_month_natural_gas, color='orange')
    years_list = [2016, 2017, 2018, 2019, 2020]
    plt.xticks(ticks=[1, 12, 24, 36, 48], labels=years_list)
    plt.title('Natural Gas')
    plt.ylabel('Therms')
    plt.show()
    elec_df = pd.DataFrame({'month': [i for i in range(1, 60 + 1)], 'value': years_data_by_month})
    gas_df = pd.DataFrame({'month': [i for i in range(1, 60 + 1)], 'value': years_data_by_month_natural_gas})
    at.Chart(elec_df, title='Electricity usage by months').mark_line().encode(x='month:N', y='value:Q').show()
    at.Chart(gas_df, title='Natural Gas usage by months').mark_line().encode(x='month:N', y='value:Q').show()


# 3
def monthly_plots():
    all_counties = total_consumption_df
    all_counties_2020_data = all_counties[all_counties['year'] == 2020]
    counties_names = all_counties_2020_data['county_name'].unique().tolist()
    counties_info = []
    for county in counties_names:
        info = []
        county_data = all_counties_2020_data[all_counties_2020_data['county_name'] == county]
        months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for m in months:
            m_data = county_data[county_data['month'] == m]
            e = m_data[m_data['data_class'] == 'electricity']['value'].tolist()
            n = m_data[m_data['data_class'] == 'natural_gas']['value'].tolist()
            try:
                e = e[0]
                n = n[0]
            except IndexError:
                pass
            counties_info.append({'county_name': county, 'month': m, 'electricity': e, 'natural_gas': n})
    at.Chart(pd.DataFrame(counties_info)).mark_point().encode(x='electricity:Q', y='natural_gas:Q',
                                                              tooltip=['county_name']).properties(width=150,
                                                                                                  height=100).facet(
        facet='month:N', columns=4).show()
