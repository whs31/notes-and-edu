% 12y'''(t) + 53.2y''(t) + 4.4y'(t) + y(t) = 10
% y(0) = y'(0) = y''(0) = 0
% on interval t \in [0, 160]

%% Аналитическое решение
syms y(t) 
dy = diff(y, t);
d2y = diff(y, t, t);
d3y = diff(y, t, t, t);
ode = 12 * d3y + 53.2 * d2y + 4.4 * dy + y == 10;

% Начальные условия
conditions = [y(0) == 0, dy(0) == 0, d2y(0) == 0];

Y = dsolve(ode, conditions);
YSimplified = simplify(Y);

% График
t_range = linspace(0, 160, 1000); 
YNumeric = double(subs(YSimplified, t, t_range));
figure(1);
plot(t_range, YNumeric);
title("Аналитическое решение ЛДУ");
xlabel("t");
ylabel("y(t)");
grid on;
disp("[1]   y(t) = " + string(Y));
disp("[1.1] y(t) = " + string(YSimplified));


%% Метод Адамса-Башфорта 1-го порядка
adams_bashforth_1(0.01);

%% Метод Рунге-Кутты (ode45)
runge_kutta();

%% Сравнение погрешностей
t_start = 0;
t_end = 160;
h = 0.2;
y_h = adams_bashforth_1(h);
y_2h = adams_bashforth_1(2 * h);
y_halfh = adams_bashforth_1(0.5 * h);
[t_rk, y_rk] = runge_kutta();
y_analytic = dsolve('12 * D3y + 53.2 * D2y + 4.4 * Dy + y = 10', 'y(0) = 0', 'Dy(0) = 0', 'D2y(0) = 0', 't');
tvec = linspace(t_start, t_end, n);
y_fn = matlabFunction(y_analytic);
y_a = y_fn(tvec);

diff_h = y_h - interp1(tvec, y_a, t_start:h:t_end);
diff_2h = y_2h - interp1(tvec, y_a, t_start:h * 2:t_end);
diff_halfh = y_halfh - interp1(tvec, y_a, t_start:h / 2:t_end);
diff_rk = y_rk - interp1(tvec, y_a, t_rk);

figure(4);
subplot(1, 1, 1);
plot(t_start:h * 2:t_end, diff_2h, 'r-', 'LineWidth', 2);
hold on;
plot(t_start:h / 2:t_end, diff_halfh, 'b--', 'LineWidth', 2);
plot(t_rk, diff_rk, 'g-.', 'LineWidth', 2);
plot(t_start:h:t_end, diff_h, 'y-', 'LineWidth', 2);
hold off;
title("Сравнение относительно аналитического решения");
legend('Адамс-Башфорт 1-го порядка, h = 0.4', 'Адамс-Башфорт 1-го порядка, h = 0.1', 'Рунге-Кутты', 'Адамс-Башфорт 1-го порядка, h = 0.2');
grid on;


%% Определения функций
function res = adams_bashforth_1(h)
    ibegin = 0;               % Начало интервала
    iend = 160;               % Конец интервала
    n = (iend - ibegin) / h;  % Количество шагов
    t = ibegin:h:iend;        % Вектор времени

    disp ("h = " + string(h));
    disp ("n = " + string(n));
    y1 = zeros(1, n + 1);
    y2 = zeros(1, n + 1);
    y3 = zeros(1, n + 1);

    % Начальные условия
    y1(1) = 0;
    y2(1) = 0;
    y3(1) = 0;

    % Метод Адамса-Башфорта по вычисленной разностной схеме
    for i = 1:n
        y1(i + 1) = y1(i) + h * y2(i);
        y2(i + 1) = y2(i) + h * y3(i);
        y3(i + 1) = y3(i) + h * ((10 - y1(i) - 4.4 * y2(i) - 53.2 * y3(i)) / 12);
    end

    figure(2);
    plot(t, y1, 'r-', t, y2, 'b', t, y3, 'g');
    legend("y(t)", "y''(t)", "y'''(t)");
    title("Решение ЛДУ методом Адамса-Башфорта 1-го порядка");
    xlabel("t");
    ylabel("y(t)");
    grid on;
    %disp("[2] y(t) = " + string(y3(end)));

    res = y1(end);
end

function [t, res] = runge_kutta()
    [t, y] = ode45(@odefunction, [0 160], [0, 0, 0]);

    % График
    figure(3);
    plot(t, y(:,1), 'r-', 'LineWidth', 2)
    hold on;
    plot(t, y(:,2), 'b--', 'LineWidth', 2);
    plot(t, y(:,3), 'g-.', 'LineWidth', 2);
    hold off;
    legend("y(t)", "y''(t)", "y'''(t)");
    title('Решение ЛДУ методом Рунге-Кутты с использованием функции ode45');
    xlabel('t');
    ylabel('y(t)');
    grid on;

    % Вывод решения
    %disp('The solution y(t), y''(t), and y''''(t) at the specified time points:');
    %disp(table(t, y(:,1), y(:,2), y(:,3), 'VariableNames', {'Time', 'y', 'dy/dt', 'd2y/dt2'}));

    res = y(end, 1);
    
    function dydt = odefunction(t, y)
        dydt = zeros(3, 1);
        dydt(1) = y(2);   
        dydt(2) = y(3);
        dydt(3) = (10 - y(1) - 4.4 * y(2) - 53.2 * y(3)) / 12;
    end
end