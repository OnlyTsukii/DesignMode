def process_and_plot(file_path, delimiter=',', fill_value=None, cols=None, stats=False, plot=False, plot_cols=None, figsize=(10, 6)):
    data = pd.read_csv(file_path, delimiter=delimiter)
    if fill_value is not None:
        data.fillna(fill_value, inplace=True)
    if cols:
        data = data[cols]
    if stats:
        print(data.describe())
    if plot:
        plt.figure(figsize=figsize)
        if plot_cols is None:
            plot_cols = data.columns
        for col in plot_cols:
            data[col].plot(kind='hist', alpha=0.5, label=col)
        plt.legend()
        plt.show()
    return data