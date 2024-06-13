%% LU разложение без выбора ведущего элемента 
% A*x = b
%     | 1 -2 -1  1 |       |  1 |
% A = | 1 -8 -2 -3 |,  b = | -2 |
%     | 2  2 -1  1 |       |  7 |
%     | 1  1  2  1 |       |  1 |

A = [1 -2 -1  1; 1 -8 -2 -3; 2  2 -1  1; 1  1  2  1];
B = [1; -2; 7; 1];

[L, U] = lu_factorize_without_pivoting(correct_matrix(A));
y = L\B;
x = U\y;
fprintf('L = %s,\nU = %s,\nx = %s\n', mat2str(L), mat2str(U), mat2str(x));

% Исходная матрица является вырожденной, поэтому в соответствии с пунктом 3 задания
% предложено изменение условия таким образом, чтобы СЛАУ можно было решить заданным методом,
% а именно: 
%     | 1 -1 -1  1 |
% A = | 1 -8 -2 -3 |
%     | 2  2 -1  1 |
%     | 1  1  2  1 |
function a = correct_matrix(a)
    epsilon = 1;
    a(1, 2) = a(1, 2) + epsilon;
end

function [l, u] = lu_factorize_without_pivoting(a)
    n = size(a, 1);
    l = eye(n);
    u = a;
    
    for k = 1:n - 1
        for i = k + 1:n
            factor = u(i, k) / u(k, k);
            l(i, k) = factor;
            u(i, k:n) = u(i, k:n) - factor * u(k, k:n);
        end
    end
end