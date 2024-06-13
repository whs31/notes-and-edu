% read_signal
% reads csv file and returns table without first row and stripped by min_x value (epsilon)
function res = read_signal(filename, min_x)
    res = readtable(filename, "VariableNamingRule", "preserve");
    res(1, :) = [];
    res = strip_by_epsilon(res, 1, min_x);
end
