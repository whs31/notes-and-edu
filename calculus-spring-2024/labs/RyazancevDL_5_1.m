%% Вычисление собственных значений матрицы (QR-алгоритм и встроенная функция)
%      | 6 8 -2 |
%  A = | 1 4  1 |
%      | 2 8  2 |
A = [6, 8, -2; 1, 4, 1; 2, 8, 2];
fprintf("QR-алгоритм:        %s\nВстроенная функция: %s\n", mat2str(eigenvalues_qr(A, 100)), mat2str(eig(A)));

function res = eigenvalues_qr(mtx, max_iterations)
    for i = 1:max_iterations
        [Q, R] = qr(mtx);
        mtx = R * Q;
    end
    res = diag(mtx);
end