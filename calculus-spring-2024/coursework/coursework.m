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
title("Analytical solution of the ODE");
xlabel("t");
ylabel("y(t)");
grid on;
disp("[1] y(t) = " + string(YSimplified));


%% Метод Адамса-Башфорта 1-го порядка
ibegin = 0;               % Начало интервала
iend = 160;               % Конец интервала
n = 1000;                 % Количество шагов
h = (iend - ibegin) / n;  % Шаг
t = ibegin:h:iend;        % Вектор времени

y1 = zeros(1, n + 1);
y2 = zeros(1, n + 1);
y3 = zeros(1, n + 1);

% Начальные условия
y1(1) = 0;
y2(1) = 0;
y3(1) = 0;

% Метод Адамса-Башфорта
for i = 1:n
    y1(i + 1) = y1(i) + h * y2(i);
    y2(i + 1) = y2(i) + h * y3(i);
    y3(i + 1) = y3(i) + h * ((10 - y1(i) - 5.5 * y2(i) - 53.2 * y3(i)) / 12);
end

figure(2);
plot(t, y1, 'r', t, y2, 'b', t, y3, 'g');
legend("y(t)", "y''(t)", "y'''(t)");
title("Solution of the ODE using Adams-Bashforth 1st order method");
xlabel("t");
ylabel("y(t)");
grid on;
disp("[2] y(t) = " + string(y3(end)));

%% Метод Рунге-Кутты (ode45)
% Начальные условия
y0 = [0, 0, 0];
tspan = [0 160];

% Решение
[t, y] = ode45(@odefunction, tspan, y0);

% График
figure(3);
plot(t, y(:,1), 'r-', 'LineWidth', 2)
hold on;
plot(t, y(:,2), 'b--', 'LineWidth', 2);
plot(t, y(:,3), 'g-.', 'LineWidth', 2);
hold off;
legend("y(t)", "y''(t)", "y'''(t)");
title('Solution of the ODE using ode45');
xlabel('t');
ylabel('y(t)');
grid on;

% Вывод решения
disp('The solution y(t), y''(t), and y''''(t) at the specified time points:');
disp(table(t, y(:,1), y(:,2), y(:,3), 'VariableNames', {'Time', 'y', 'dy/dt', 'd2y/dt2'}));

function dydt = odefunction(t, y)
    dydt = zeros(3, 1);
    dydt(1) = y(2);   
    dydt(2) = y(3);
    dydt(3) = (10 - y(1) - 4.4 * y(2) - 53.2 * y(3)) / 12;
end