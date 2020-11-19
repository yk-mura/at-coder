N, Q = map(int, input().split())
C = list(map(int, input().split()))

grp_no_list = [i for i in range(1, N + 1)]

for _ in range(Q):
    query = input()

    if query.startswith('1'):
        _, a, b = map(int, query.split())

        a_grp_no = grp_no_list[a - 1]
        b_grp_no = grp_no_list[b - 1]

        # Bグループの生徒のIdx
        b_grp_std_idx_list = [std_idx for std_idx, grp_no in enumerate(grp_no_list) if grp_no == b_grp_no]

        # BグループをAグループに合流
        for idx in b_grp_std_idx_list:
            grp_no_list[idx] = a_grp_no

    else:
        _, x, y = map(int, query.split())

        # Xグループの生徒のIdx
        x_grp_no = grp_no_list[x - 1]
        x_grp_std_idx_list = [std_idx for std_idx, grp_no in enumerate(grp_no_list) if grp_no == x_grp_no]

        # Yクラスの生徒のIdx
        y_cls_std_idx_list = [std_idx for std_idx, cls_no in enumerate(C) if cls_no == y]

        # XグループとYクラス両方に所属する生徒のIdx
        x_and_y = set(x_grp_std_idx_list) & set(y_cls_std_idx_list)

        print(len(x_and_y))
