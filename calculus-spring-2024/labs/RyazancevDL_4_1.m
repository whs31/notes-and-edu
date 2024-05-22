%% Метод бисекции
% x^3 - 0.2x^2 + 0.5x + 1.5 = 0

f = @(x) x^3 - 0.2 * x^2 + 0.5 * x + 1.5;
solve_nonlinear_equation(f, -10, 10, 1e-6);

function root = solve_nonlinear_equation(f, lower_bound, upper_bound, tolerance)
    max_iterations = 100;
    iter_count = 0;
    while iter_count < max_iterations
        mid_point = (lower_bound + upper_bound) / 2;
        f_mid = f(mid_point);
        f_lower = f(lower_bound);

        if f_mid * f_lower < 0
            upper_bound = mid_point;
        else
            lower_bound = mid_point;
        end

        if abs(f_mid) < tolerance
            fprintf("Root found: x = %f\n", mid_point);
            root = mid_point;
            return
        end
        iter_count = iter_count + 1;
    end
    fprintf("Max iterations reached. Approximate root: x = %f\n", mid_point);
    root = mid_point;
end