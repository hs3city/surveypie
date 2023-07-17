
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# the data taken from here https://github.com/ourcodingclub/CC-Qualit

sust_behaviour = pd.read_csv("/content/sust_behaviour.csv")
sust_lookup = pd.read_csv('/content/sust_lookup.csv')

sust_data = sust_behaviour['sustainability_daily_think'] = pd.Categorical(sust_behaviour['sustainability_daily_think'],
                                                         categories=["Never", "Rarely", "Sometimes", "Often", "All the time"],
                                                         ordered=True)

sust_think_summ_wide = sust_behaviour.groupby(['gender', 'sustainability_daily_think']).size().reset_index(name='n')
sust_think_summ_wide['perc'] = sust_think_summ_wide['n'] / sust_think_summ_wide.groupby('gender')['n'].transform('sum') * 100
sust_think_summ_wide = sust_think_summ_wide.drop('n', axis=1)
sust_think_summ_wide = pd.pivot_table(sust_think_summ_wide, values='perc', index='gender', columns='sustainability_daily_think')

sust_think_summ_wide

sust_think_summ_hi_lo = (sust_think_summ_wide.assign(midlow=lambda x: x.Sometimes / 2, midhigh=lambda x: x.Sometimes / 2))
sust_think_summ_hi_lo = sust_think_summ_hi_lo.filter(['gender', 'Never', 'Rarely', 'midlow', 'midhigh', 'Often', 'All the time'])
sust_think_summ_hi_lo = sust_think_summ_hi_lo.reset_index()
sust_think_summ_hi_lo = sust_think_summ_hi_lo.melt(id_vars =['gender'],var_name='response', value_name='perc')
sust_think_summ_hi_lo = sust_think_summ_hi_lo.rename(columns={'variable': 'response'})

sust_think_summ_hi_lo

sust_think_summ_hi = sust_think_summ_hi_lo[
    sust_think_summ_hi_lo["response"].isin(["All the time", "Often", "midhigh"])
].copy()

sust_think_summ_hi["response"] = pd.Categorical(
    sust_think_summ_hi["response"],
    categories=["All the time", "Often", "midhigh"],
    ordered=True
)

sust_think_summ_hi

sust_think_summ_lo = sust_think_summ_hi_lo[
    sust_think_summ_hi_lo["response"].isin(["midlow", "Rarely", "Never"])
].copy()

sust_think_summ_lo["response"] = pd.Categorical(
    sust_think_summ_lo["response"],
    categories=["Never", "Rarely", "midlow"],
    ordered=True
)

sust_think_summ_lo

legend_pal = plt.cm.RdBu(np.linspace(0, 1, 5))
legend_pal
legend_pal = np.insert(legend_pal, 3, legend_pal[3], axis=0)
legend_pal
legend_names = ["All the time", "Often", "midhigh", "midlow", "Rarely", "Never"]
legend_pal_dict = {name: color for name, color in zip(legend_names, legend_pal)}
legend_pal_dict

# plot from tutorial

plt.barh(sust_think_summ_hi['gender'], sust_think_summ_hi['perc'])
plt.barh(sust_think_summ_lo['gender'], -sust_think_summ_lo['perc'])
legend_pal = ["All the time", "Often", "midhigh", "Rarely", "Never"]
plt.legend(handles=legend_names, labels=["All the time", "Often", "Sometimes", "Rarely", "Never"])
plt.xlabel("Gender")
plt.ylabel("Percentage of respondents (%)")
#plt.title(sust_lookup['survey_question'][sust_lookup['column_title'] == "sustainability_daily_think"])

#Here is Paweł solution

# Female plot
print(list(sust_think_summ_lo['response'][0::2]))
print(list(sust_think_summ_lo['perc'][0::2]))
# Male
print(list(sust_think_summ_lo['response'][1::2]))
print(list(sust_think_summ_lo['perc'][1::2]))


sust_think_summ_f = sust_think_summ_hi_lo[sust_think_summ_hi_lo['gender'] == 'Female']

species = (
    "Female", "Male"
)
weight_counts = {
    name: np.array([perc_m, perc_f]) for name, perc_f, perc_m in zip(sust_think_summ_hi_lo['response'][0::2], sust_think_summ_hi_lo['perc'][0::2], sust_think_summ_hi_lo['perc'][1::2])
}
print({
    name: np.array([perc_m, perc_f]) for name, perc_f, perc_m in zip(sust_think_summ_hi_lo['response'][0::2], sust_think_summ_hi_lo['perc'][0::2], sust_think_summ_hi_lo['perc'][1::2])
})

width = 0.5
fig, ax = plt.subplots()
bottom = np.zeros(2)

for boolean, weight_count in weight_counts.items():
    p = ax.barh(species, weight_count, width, label=boolean, left=bottom)
    bottom += weight_count

ax.legend(loc="upper right")
plt.show()

