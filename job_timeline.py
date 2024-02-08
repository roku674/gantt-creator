# Re-importing necessary libraries after code execution state reset
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Re-defining the timeline data
timeline_data = [
    ["Software Engineer - Optimized Payments", "2022-11-01", datetime.today().strftime('%Y-%m-%d')],
    ["Software Engineer - MagMutual", "2021-03-01", "2022-11-30"],
    ["Warehouse Associate - CAPCO, Capital Materials Inc.", "2019-09-01", "2020-01-31"],
    ["Personal Project - Perilous Games", "2017-01-01", datetime.today().strftime('%Y-%m-%d')],
    ["Intern - A&R Engineering", "2017-05-01", "2017-08-31"],
    ["Intern - A&R Engineering", "2016-05-01", "2016-08-31"],
    ["Intern - Arcadis U.S. Smyrna, GA", "2015-05-01", "2015-08-31"],
    ["Intern - Arcadis U.S. Smyrna, GA", "2014-05-01", "2014-08-31"],
    ["Cryptocurrency Miner - Mining", "2014-12-01", "2020-12-31"]
]

# Convert dates to datetime objects for plotting
for i, item in enumerate(timeline_data):
    start_date = datetime.strptime(item[1], '%Y-%m-%d')
    end_date = datetime.strptime(item[2], '%Y-%m-%d')
    timeline_data[i][1] = start_date
    timeline_data[i][2] = end_date

# Generate the timeline with distinct colors for each job
colors = plt.cm.get_cmap('tab20', len(timeline_data))

fig, ax = plt.subplots(figsize=(10, 8))

# Plot each job with a different color from the colormap
for i, (job, start, end) in enumerate(timeline_data):
    ax.plot([start, end], [i] * 2, marker='|', markersize=12, color=colors(i), label=f'{job}')

# Improve layout with non-green colors
ax.yaxis.set_visible(True)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=45)
plt.title('Job Timeline')
plt.legend(loc='lower left')

plt.tight_layout()
plt.show()
