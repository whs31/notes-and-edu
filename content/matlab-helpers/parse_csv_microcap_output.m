%% parse_csv_microcap_output

sig = read_signal('example.csv', 0.006);

sig = sig{:,:};
sig = sig(:,2);
max_value = max(sig);