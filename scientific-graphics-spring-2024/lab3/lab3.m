%% surf (default)
[x, y] = meshgrid(1:0.1:10, 1:0.1:10);
z = cos(x) + sin(y) * cos(x);
figure; surf(x, y, z);
title('График с использованием функции surf'); xlabel('x'); ylabel('y')
disp('График построен (1)')

%% surf (gray)
[x, y] = meshgrid(1:0.1:10, 1:0.1:10);
z = cos(x) + sin(y) * cos(x);
figure; surf(x, y, z);
title('График с использованием функции surf (ч/б)'); xlabel('x'); ylabel('y')
colormap(gray)
disp('График построен (2)')

%% plot3 (default)
[x, y] = meshgrid(1:0.1:10, 1:0.1:10);
z = cos(x) + sin(y) * cos(x);
figure()
plot3(x, y, z); grid
title('График с использованием функции plot3'); xlabel('x'); ylabel('y')
disp('График построен (3)')

%% plot3 (styled)
[x, y] = meshgrid(1:0.1:10, 1:0.1:10);
z = cos(x) + sin(y) * cos(x);
figure()
plot3(x, y, z, 'diamond', 'Color', '#7E2F8E', 'MarkerSize', 3); grid
title('График с использованием функции plot3 (с оформлением)'); xlabel('x'); ylabel('y')
disp('График построен (4)')

%% mesh (default)
[x, y] = meshgrid(1:0.1:10, 1:0.1:10);
z = cos(x) + sin(y) * cos(x);
figure()
mesh(x, y, z); 
title('График с использованием функции mesh'); xlabel('x'); ylabel('y')
disp('График построен (5)')

%% mesh (styled)
[x, y] = meshgrid(1:0.1:10, 1:0.1:10);
z = cos(x) + sin(y) * cos(x);
figure()
mesh(x, y, z); 
title('График с использованием функции mesh (с оформлением)'); xlabel('x'); ylabel('y')
disp('График построен (6)')
colormap(cool)