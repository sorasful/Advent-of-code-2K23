import re
from collections import defaultdict

text = """Card   1: 10  5 11 65 27 43 44 29 24 69 | 65 66 18 14 17 97 95 34 38 23 10 25 22 15 87  9 28 43  4 71 89 20 72  5  6
Card   2: 25 43 15 31 45 19 36 73 34 85 | 92 11 85 68 74 20 19 71  1 36 43 32 77 33 14 31 73 15 45 83 34 25  6 88 57
Card   3:  4 46 42 23 18 98 59 75 19 57 | 22  3 75 80 42 23 59 39 98 38 18 21 67 57 20 25 71 26 64  4 83 79 91 65 90
Card   4: 92 13 56 27 19 44 70 93 32 66 | 38  4 19 75 87 93 32  1 23 14 51 22 42 44 33 63 13 56 70 66 18 92 47 53 27
Card   5: 25 18 30 45 23 80 91 13 47 61 | 62 45 71 30 39 19 61 68 23 80 91 96 25 58 13 88 67 29 60  2 74 55 12 83 46
Card   6: 20 36 26 18 61 35 94 58 79 19 | 85 68 56  7 53 58 19 20 79 59 26 61 18 15 94 33 29 71 35 89 17 36  3 67 72
Card   7: 29 21 71 91 74  6 12 53 50 55 | 29 51 12 74 82 18 21 55 53 33 65 91 95 69  2 62 57 50  3 79 71 61 47  6 14
Card   8: 24 72 46 88 65 12 48 97 76 73 | 17 97 87 18 83 11 49 44 88 79 64 55 19 25 63 74 73 14 82 15 72 43 76 48 46
Card   9: 86 38 55 52 33 61 41 75 87 26 | 38 97 88 91 33 36 54 64 40 52 68 71 43 55 72 75  4 61 58 49 56 86 30 15 17
Card  10: 15 37 72  5 66 81 33  6 80 76 | 52 34 21 68 72 82 91 81  7 19 86 67 94 87 16 63 43  9 14 23 44 60 18  4 74
Card  11: 24 21 17 27 34 80 18 79 56 32 | 18 45 21 63 82 69 48 54 89  5 83 80 92 93 49  8 55 12 97 35  4  3 42 94 56
Card  12: 90 61 45 54 64 93 69 85 58 88 | 79 89 74 45 27 61  9 56 69 88 13 80 66  4 16 62 34 51 71 54 48 64 58 63 50
Card  13: 80 39 35 27 56 94 25 77 84 26 | 24 19 72 54 96 63 56 15 25 16 59 35 20 57 52 65 95 66 45 31 77 60 42 93 37
Card  14: 33 83 94 41  7 79 18 40 24 97 | 49 27 45 21 20  8 93 26 12 42 94 33 96 57 98 91 19 52 78  2 18 80 65 72 44
Card  15: 16 83 92 40 13 35 94 23 47 17 | 55 61 75 43 18  5 22 65 67  7 49 63 71 13 45 78 53 21 57 34 98 99 64 32 56
Card  16: 14 76 72  8 42 61 60 82 24 21 | 56 10 38 11 37 45 29 22 51 98 86 49 26 13 16 52 50 14 70 30 87 73 66 77 88
Card  17: 63 32 83 13 81 89 33 49  5 34 | 99 85 12  6 27 93 78 44 14 76  1 51 36  9  4 62 91 84  8 37 45 66 75 42 40
Card  18: 43 97 37 61 69 94 60 67 91 99 | 87 25 65 98 26 62 42 11 61 32 34 76 14 20 44 92 22  5 12 46 21 33  3 15 59
Card  19: 32 96 10 49 26 86 67 85 50 75 | 58 98 84 43 23 33 64 74 37 80 63 40 51 95 13 55 31 25 87 97 81 52 53 24  6
Card  20:  7 70 41 40 16 15 20 72 47 93 | 93 41  7 79 62 86 69 70 75 67 51 72 81 15 22 48 47 80 71 38 40 97 20 82 16
Card  21: 90 76 52 48 36 37 89 45 20 17 | 23 48 86  7 99 50 20 58 93 43 16 91  5 76 52 45 17 68 89 22 61 36 90 37 83
Card  22: 85 71 20 58 32 83 53 94 61 80 | 88 59 66 80 49 53 19 97  5 20 62  8 94 54 67 73 93 12 10 61 32 41 71 72 85
Card  23: 60 61 30 65 11 28 89 54 22 78 | 88 71 97 46 60 45 54 26 22 42 59 57 80  9 69 61 47  3 85  7 32 78 11 66 33
Card  24: 35 16  5 85 87 58 66 39 88 12 | 51 32 59 41 73 21 58 79 72 10 74 28 95 69 16 92 88 18 34 46 77 17 65 76 99
Card  25: 67 41 62 96 40 22 81 12 98  9 | 92 66 87 35 50 38 19 14 74 93  1 76 59  6 84 99 58 61 34 13 63 30 53 90 24
Card  26: 10 78 28  1 72 94 60 71 37 89 | 71  9 28 11  4 72 43 90 74 37 18 14 40 16 21 97 59 13 73 89 63 60  5 10 70
Card  27: 65  7 45 59 32 51 22 16  2 64 | 65 37 72  7 26 86 49  3 63 67 16 52 51 21 89 14 70 78 36 27 92 39  8 64 42
Card  28: 89 17 93 57 78 33 52 97 53  4 | 23 20 66 55 42 28 52 61 35 41 60 51 84 83 49 67 22  5 48  9  2  7 87 38 93
Card  29: 64 12 30 16 87 59 76 34 85 28 | 47 21 32 37 94 25  6 26 49 59 81 45 87 70 23  5 91  8 34 58 72 89 52 93 63
Card  30: 11 69 86 19 59 28 41 68 81 66 | 92 33  1 43 88 75 42 29 38 55 24 89  4 95 47 70 30 65 83 72 25 82 14 85 21
Card  31: 48 43 14 54 80 70 93 64 42 77 | 91 19 62 79 30 23 29 11 37 13 41 54 97 52  7 90 33 17 96 28 20  9 47 31 38
Card  32: 78 91  2 56 93  3 88 50 20 12 |  2 20 18 84 12 82 43 76 39 53 32 79 57 17 63 28 30  9  1 55 96 70 29 25 87
Card  33: 99 93 14 28 36 68 11 97 58  9 | 94  4 67 66 40 87 96 83 78 23 71 41 92 24 77  1 15 42 12 57  3 89 46 72 59
Card  34: 20 88 61 67 31 21 90 30 26 56 |  6 71 18 34 66 10 41 37 58 32 13 76  3 96 86 47 50 91 17 15 39 68 73 27 12
Card  35:  5 58 96 48 47 70 19 34 63 84 | 21 59 88 32 37 33 20 49 55 62  7 66  1  2 40 77 22 82 39 13 45 61 56 44 17
Card  36: 36 66 44 13 33  2 60 46  4 31 | 73 99 13 72 44 80 60 77 65 19 46  4 59 97 61 98 31 92 83  2 68 36 66 33 22
Card  37: 95 71 87 60 17 19 97 30 48 55 | 30 53 35 19 94 27 95 44 47 13 69 87 12 56  4 26 85 17 63  7 70 60 71 41  3
Card  38: 61 16 20 92 98 19 79 62 45 91 | 79 44 60 23 25 83 92 19 16 38 66 48 75 20  2 98 24 87 45 62 61 32 91 69 13
Card  39: 49  2 18 74 99 30 54 16 93 68 |  8 74 75 72 68 67 89 86 31 30 97 47 24 71 18 99 54 22 16 70  3  7 49 50 25
Card  40: 12 45  7 15 65 84 77 36 28  1 | 51 35 63 43 59 81 88 58 56 71 94 46  9 86 28 13 30 99 20 17 95 23 32 54 47
Card  41:  8 99 26 60 56 69 48 47 31 16 | 83  9 66 73 95 67 21 86 94  2 99 51 98 80 57 36 82  4 23 19 12 68 88 44 59
Card  42: 99 48 94 50 91 55  2 12 67 36 | 47 45 62 66 31 84 26 20 52 41 40 55 21 35 37 15 69 53 72 65 79 60 25 48 57
Card  43: 41 75 61 39 67 88 48 42 51 79 | 85 99 95 79 64 92 34  8 46 15 56 28 12  6 81 48 41 49 20 97 91 67 51 55 74
Card  44: 10 99 33 96 21  6 49 62 82 38 | 68 41 88 24  6 28 98 66 96 49 30 33 94 85  1 75 21 61 60 99 89 81 31 54 20
Card  45: 46 61 60  2 29 45  7 55 83 16 | 25 34 84 91 97 61 55 17 16 79 67 53 59 27 69 58 29 46 24 93  3 32 60 49 33
Card  46: 93 25 42 68 22 85 58 61 63 50 |  8 46  4 15 96 83 94 13 19 65 24 80 64 38 89 44 52 78 98 36 47 51 97  2 57
Card  47: 11 59 80 10 72 76 43 86 56  7 | 59 67 35  5 47 81 99 21 38 90 73 55 64 24 34 42 58 51 56 11 68 60 23 92 43
Card  48: 97 88 28 44 24 10 17 27 83 12 | 67 92 74 50  4 35 77 47  6 40 11 20 76 16 42  9  3 79 68 82 43 41 60 94 89
Card  49: 35 98 90 92 42 12 13 83 53 95 | 36 34 51 96 24 94 53  7 31  6 71 48 16 75 77 83 68 46 14 66 65 22  9 74 93
Card  50:  1 65 66  2 76 36 78 56 99 90 | 12 13  3 38 96 20 10 14 57 81  7 35 88 55 68 48 31 52 89  9 70 15 79 80 16
Card  51: 70 41 53 40 55 82 69  7  5 71 | 56  4 54 46 65 17 91 94 72 88 90 31 85 14 97 95 44 26 92  8 21 73 38 77 37
Card  52: 62 16 85 42 56  1 82 92 43 37 | 74 28 19 42 82 21 85 37 75 50 17 16  1 76 56 86 91 31  3 92  6 62 43 64 83
Card  53: 69 91 12  9 63 50 58 57 67 13 | 40 42 70 62  6 69  9 82 78 19 89 56 57 83 47 25 98 46 30 53 72 28 10 58 44
Card  54: 73 44 64 21 16 50 63 41 36 51 |  6  4 66 39 21 14 67 50 15  1 35 40 64 44 24 73 28 47 80 13  2 43 91 46 16
Card  55: 47 55 14 43  1 54 81 65 19 33 | 19 10 97 44 84 61  5 25 96 81 32 73 75 83 65 17  3 41 14 92  9 80 27 63  8
Card  56: 43 26 93 75 33 51 89 60  1 81 |  9 10 16 60 84 81 93 26  4 96 17 91 79 18 43 67 47 92  1 33 21 63 51 75 89
Card  57: 76 70  7 31  8 39 63 99 30 13 | 31 63 76 17 68 39 30 50 27 72 84 79 70 57 28 13 29 97 67  8 75 87  3  7 99
Card  58: 28 29 86 65  7 36 38  3 20 43 | 70 20 65 64 43 98 18 19 78 87  7 55 30 35 28 37 56 29 39 38  3 40 36 86 75
Card  59: 55 10 23 31 17 37 22 92 14 44 | 67 11 60 92 42 68 44 78  3 43 76 16 97 55  8 35 49 54 18 40 46 52 95 84 69
Card  60: 34 13 63 27 44 11 80  9 43 28 | 48 44 95 59 41 13 30 40 73 33 10 19 74 14 78 12 37 28 35 63 87 39 53 11 93
Card  61: 42 75  7 20 73 47 16 28  5 92 | 12 65  7  5 38 74 58 28 62 85 10 47 18 75 86 52 73 77  1 43 36 93 80 13 20
Card  62: 47 35 92 12 61 25 83 96  6 87 |  5 21 56 66 24 13 19 54 68 92 87 12 93 35 88 11 49 79 69 31 42 96 47 59 84
Card  63: 43 97 21 67 11 40 81 53 23 42 | 65 52 24 80 71  6  3 88 72 17 66 77 41 57 44 91  1 36 56 27 39 43  8 67 34
Card  64: 96 73 20 69 19 93 98 99 41 24 | 20 19 52 63 60 34  8 40 14  6 89  1 94 62 98 96 22 71 65 35 28 18 25 59 42
Card  65:  5 40 14 19 36 93 59  9 12 75 | 60 15 90 21 71 66 86 59 62 31 82 76 38 14  9 98 53 32  6  8 19  4 11 33 29
Card  66: 97 35 40  5 62 15 79 72 38 32 | 69  8 94 75 35  9 64 96 42 76 67 91 31 92 52 71 77 45 18 12 61 25 88 20 50
Card  67: 55 89 12 98 71 16 36 87 91 25 | 32 39 83 13 10 81 51 29 43  7 70 60 40 78 44 17 23 94 57 22 20 11 86 34 99
Card  68: 53 37 26 55 34 39 62 35 68 86 | 44 85 58 41 42 31 52 35 66 49 77 65 27 60  7  2 45 21 26 40 20 18 69  4 99
Card  69: 45  7 89 51 21 97 38 33 84 28 | 72 39 65 64 24  1 62 56 54 12  5 60 80 49 88 26 42 19 71 46 87 70  9  8 82
Card  70: 50 92 10 16 56 40 14  6 61 30 | 11 68 37  3 74 32 58 66 18 20 69 33 22 19 97  7 53 39 64 91 57 55 51 87 83
Card  71: 16 38 60 51 15 56 26 46 76 64 | 26 65 51 88 63 56 64 76 61 40 20 16 55 81 29 58  7 38 46 62 37 23  4 15 60
Card  72: 48  3 37  4 61  7 63 69 18 38 |  7 63 22 48  8 91  2 77 40 44 69 86 51 74 37 53 38 96 49  3  4 61 18 15 43
Card  73: 22 59 55 78 44 99 96 29 76 46 | 59 23 44 31 29 63 18 92 46 22  4 56 85 43 82 94 95 48 14 64 78 76 55 99 96
Card  74: 49 46 66 52 68 64 62 93 81 96 | 83 31 15 98 68 17 74 79 81 20 25 66 16 53 43 46 30 21 24 70 63  1 82 71 72
Card  75: 25 56  3 78 52 87  6  5 54 99 |  1  4 66 17 87  5 52 79 88 25 36 99 86  3 65 61 70 71 78 54 56 39 69 68  6
Card  76: 62 66 78 11 51 71 42 84 39 33 | 26 29 45  7 32 58 83 72 19 82 67 91 76 59 39 93 41  5 12 47 79 49 21 11 20
Card  77: 98 80 42 61 82 18 34 66  2  1 | 84 33 16  9 91 86 22 42  1 34 46 99 41 82 85 61 49 26 18 88 98 66 80 72  2
Card  78: 74 69 73 62 50 86 14 34 15 57 | 73 40 62 15 52  9 68 82 46 86 89 22 83 74 50 58 38  8 34 16 14 69 57 64 60
Card  79: 99 36 21 35 10 43 32 69 74  6 | 10 14 75 66 48 15 17 43 74  2 16 50 56  6 69 61 87 36 99 32 90 21 35 60 28
Card  80: 63  3 55 47 54 20 95 72 36 57 | 80 57 63 66 47 44 49 38  3 54 15 52 11 75 16 72 50 55 36 95 33 81 26 45 20
Card  81: 46 61  5 40 70  1 65 18 74 78 | 70 66 57 55  9 33 83 71 78 37 74 18 92 38 65 84 40  1 97 61 91 59  5 46 24
Card  82: 85 25 81 91 76 71  8 12 24 21 | 37 76 74 34 85 91 44 41 99  8 25 28 98 39 24 12 71 75 95 47 21 69 46 81 40
Card  83: 98 57 78 67 90 55 53 74 59 85 | 20 52 73 61 41 64 85  4 68 70 87 14 32 99 55 48 84 74 94 80 50 42 25 44 35
Card  84: 22 56 11  9 47 49  1 91 78 55 | 52 28 97 67 44 37  4 61 36 53 96 30  2 19  9 43 29 15 49 41 68 72  7 38 94
Card  85: 84 66 28 12 30 82 69 57 72 76 | 37 48 69 96 47 78 98 59 43 27 29 35 15 81 32 64 66 57 94 95 44 12  2 89 70
Card  86: 47  5 23 50 56 45 25 54 60 42 | 34 71  3 94 42 46 43  5 39 83 95 27 40 18 13 14 47 59 65 12 38 11 15 82 28
Card  87: 93 58 92 44 94 78 80 26 39 50 | 75 47 94 20  9 85 79 26 56 44 14 67 95  5 12  6 31 30 39 40  8 58 80 34 59
Card  88: 61 20 91 64 69 87 50  2  8 45 | 61 14 28 67 11 91 82 51 18 52 66 24 62 59 92 69  2 49  3 46 42 35  4 27 20
Card  89: 32 38  6 48 14 60 82  1  9  5 | 97 29 67 21  7 46 12 19 65 14 34 35 44 82 64  5 40 98 57 13 45 55 10 22 79
Card  90: 89 54  9 27 86 29 17 26 20 47 | 46 51 40 60  2 41 59 89 79 47 73 52 15 29 81 84 96 22 44 13 10 72 87 28 86
Card  91: 98 15 46 26 72 22 71 82 90 39 | 63 62 29  7 90 79 12 49 54 96 21 70  6 13  2  9 86 53 99  3 33 72 66 28 22
Card  92: 65 33 98 12 70 18 47 71 69 59 | 58 66 85 27 26 43 87 51 39 83 73 33 17 54 90  5 99 29  8 49 34 71 45 19 78
Card  93: 62 50 63 30 80 74 32 70 31 12 | 28  3  9 71 34 40 12 77 55 69  2 44 76 58 83 11 23 17 10 13 33 81 93 94 85
Card  94: 21 23 14 63 32  5 70 79 81 44 |  4  1 18 35 64 58 80 42 47 92 25 78 82 11  9 83 65 86 17 90 69 56 98 85 84
Card  95: 88 44 69 23  3 34 22 59 72 10 | 30 87 25 88 72 57 34 10  3  1  4 64 44 17 42 33 20 69 93 65 73 11 23 59 22
Card  96: 51 94 55 41 65 57 59 98 39 96 | 38 54 83 39 96 94 88 65 32 41  9 55 51 73 93 59 58 63 64 98 45 57  8 33 74
Card  97:  4  5 90 20 15 14 49 40 84 11 | 73 75 29 47 15 64 53 66 74 43 50 84 12 28 90  5  3 20  4 11 40 49 14 71 95
Card  98: 74 49 44 95 50 71 77 22 41 57 |  4 75 47  3 45 82 58 53 88 69 59 17 51 68 66 67 36 25  7 14 78 12 49 73  9
Card  99: 48  4 79 15 61 85 92 45 22 81 | 30 23 78 35 17 14 24 68 90 74 37 32 46 19 79 42 22 43 50 41  7 92 39 10 15
Card 100: 26 67  9 17 82 11 34 47 10 20 | 56 10 73 34 59 62 97 67 12 48 47 20 17 90  7 40 50 13 55  9 27 65 31 38 26
Card 101: 79 10 29 36 95 26 94 40 50 89 |  6 54 33 88 74 46 67 70 51 39 94 78 31 59 37  5 56 53 36 42  1 87 29 64 40
Card 102: 50 40 34 30  2 32 95 70 10 16 | 57 66 90 83 94 31 79 67 14 93 28 52 32 22  9 43 54 39 49 40 35 21 87 78 88
Card 103: 85 35  6 42 31 71 49 17 95 55 | 61 67 34 99 52 59 46 38 51 36 73 43 94 97 91 76 37  4 25 18 30 64 41 22 26
Card 104: 89 73 65 69 94 68 28 49 19 55 | 14 33 51 92 40 70 73 91 45 20 72 21 69 43 19 52 56 27  4 37 67  1 13 80 83
Card 105: 65 98 51 74 36 45 61 87 42 50 | 70  6 30 26 84 75  1 96 37 31 53 95 24 66 40 52 72 22 44 54 77 99 25 19 69
Card 106: 35 46 52 34 28  3 36 42 80 10 | 53 43 20 22 62 75 83 11 44 85 78 39 72 90 73 18 86 16 65 19 98 47 41 45 88
Card 107: 92 17 73  3 72 57 63 66  1  9 | 61 67 98 59 31  3 48 83 33  1 72  2 13 42 50 68 19 53 15 32 14  9 49 52 23
Card 108:  9 27 28 88  4 82 63 73 36 92 | 99 45 20 57 31 94  7 22 39 55 86 79 95 62 96 58 97 12 15 56 34 40 17 51 33
Card 109: 48 43 25 17 34 83  3 19 18 86 | 61 71 38 28 96  1 36 25 16 37 52 33 67 83 50 47 10 46 51 34 11  7 77 68 80
Card 110: 36 41 13 69 51 66 48 79 60 93 | 94 80 37 81 66 97 17 73 13 35 27 67 88 29 84 57 96 77 12 75 33 85 15 82 58
Card 111: 88 65 71 66 39 67 50 42 86 99 | 20 10 87 41 45 63 31 40 64 35 97 99 53 98 72 11 85 19 79 13 22 55 24 25 34
Card 112: 75 37 68 18 90 88 42 20 50 40 | 31  5 15 80 33 66 35 69 64 97 11 92 85 94 24 65 44 22 71 36 17 12 29 39 98
Card 113: 81 60 57 44 33 56 89 36 50  1 | 27 76 64 89 85 68 42 36 22 67 32 60  4 57 74 28 16 17 44 65 14 31 43 45 12
Card 114: 34 92 35 43 65 63 29 49 48 13 | 13 16 12 31 14 75  2 30  3 37 28 11 91 50 69 72 87 52 95 85 58 94 49 19 23
Card 115: 11 80 20 25 93 96 19 99 74 58 | 41 45 39 22 19 31 20 99 25 62 37 77 58 78  3  1 81 96 56 14 32 85 83 53 57
Card 116: 86 83 81 62 55 80 77 46 53 38 | 62 80 30 83 70 54 38 51 25 46 84 81 27 53 58 55 56 41  9 77 22 49 18 86 78
Card 117: 25 95 92  2  7 30 81 76 96 61 | 12 52 25  2 34 92 82 58 96 85 76 67 70 81 16 61  7 19 37 95 18 43 45 79 30
Card 118: 91 45 52 34 15 28 48 83 67 38 | 98  6 92 67 38 79 34  4 80 48 58 91 88 72  3 33 52 73 45 89 28 63 41 54 17
Card 119: 71 82  4 62 58 44 60 34 79 14 | 40 62 82 60 58 34  3 27 22 14 72 65  4 85 53 96  7 46 11 97 35 47 67 19 71
Card 120: 63 80  9  4 94 46 66 61 81 76 | 47 35 81 21 73 23 63 38 55 65 94 76 54 15 87 43  8 72 70 75  9  3 66 80 85
Card 121: 67 50 91 52 64 43 30 75 34 85 | 95 32  8 64 43 42 85 45 98 76  7 52 80 22 46  9 36 30 15 40 54 81 44 67 57
Card 122: 19 62 83 56 46  1 47 64 25 23 | 67 50 30 79 58 90 39 80 69 20 91 37 94 65 88 98 18 92 73 33 66 44 70 11 64
Card 123: 87 36 39 75  4  6 85  9 54 82 | 44 50 45 57 27 34 86 21 97 53 93 75 39 26 61 41 81 49 51 29 13 66 37 30 87
Card 124: 74 32 61 26 52 21  3 30  5 58 | 38 69 20 31 68 60 44 61 97 79 29 66 23 62 37 94 33 54 96 71 87  1  9 50 11
Card 125: 99 26 61 20 66 13 40 62 89 29 | 66  3 60 19  8 43 48 28 70 23 45 35 64  5 42 58 95 15 56 59 44  1 51 49 80
Card 126: 51  1 62 49 98 34 36 74 73 17 | 67 92 29 10 21 59 91 89 11 15 83  9 63 99 41 60 31 73 78 25 72 96 35 87 71
Card 127: 90 94 39 24 60  8 53 14 78 27 | 54 51 77 16  1 67  6 20 15 18 71 41 81 10 66 63 13 11 64  4 58 43 83 65 98
Card 128: 43 40 76 96 65 82 15  5 23 16 | 70 24 56 40 52 71 96  7 87 91 11 75 43 41  5 45 30 33 34 15 80 27 61 76 17
Card 129: 90 76 62  9 60  2 48 87 80 52 | 10  7 96 17  8 71 47 52 59 91  1  4 33 56 58 66 92  2 37 53  9 29 25 98 13
Card 130: 88 44 46 35 38 33 86 60 40 83 | 86 92 43 88 40 26 80  4 11 54 46 44 50 60 58 33 35 83 82 48 67 18 55 89 38
Card 131: 54 34 30  7 66 16 81 71 98  9 | 57 65 78 81 98 24 34 88 96 69  7 54 41 53 63 30 52  8 71 66 59 16  9 79 11
Card 132: 51 40 52 69 64 83  5 39  2 58 | 58  5 88 83 93 56 78 50 40 63 39 62 89 52 75 81  6 43 65 55 69  2 64 33 51
Card 133: 34 96  6 68 85 44 60 66  3 64 | 67 60 64 82 53 85 55 99 44 34  6 68 66 92 70 84  3 45 88 19 78 24 74 96 49
Card 134: 60 85 79 76  9 68 49 67  5 44 | 79  2 68 59 76 14  3 96 67 13  7 73 88  4 77 71 43 44 11  5 27 95 60 80 20
Card 135: 24 84 80 20 88 19 73 22 74 56 | 67  3 13 94 50  6  8 98 87 68 17 82 99 77 14 32 23 72 93 95 60 53 41 48 51
Card 136: 40 21 95 86 63 78 61 49 14 67 | 92 84 85 79 55 56 96 52 34 22 57 26 65 93 43  5 50  8 36 94 46 30 97 64 80
Card 137: 89 69 19 24 83 11 97 42 18  9 | 43 38 89 82 75 14  9 58 24 29  4 19 46 42 11  2 23 97 67 17 18 69 83 81 16
Card 138: 70 72 41 78 17 85 93 97 99 73 | 11 93 97 81 52 17 49 10 91 20 99 58 13 89 74 47 70 23 65 90  7  4 64 28 85
Card 139: 18 38 96 48 37 73 80 89  7 19 | 77 13  3 51  4 45 76 21 93 33 43 47 57 17 24 11 35 75 59 60 44  5 90 55 32
Card 140: 52  2 39 85 65 97  5 87 20 90 | 42 26 34 60 65 50 90 94 23 84 73 16 89 37 79  3 17 55 33 14  9 98 70 96 56
Card 141: 85 56 58 55 62 47 92 76 95 89 | 41 58 67 78  4 61 10 17 23  1 50 21 18 90 45 94 15 37 48 31 91 54 73 35 64
Card 142: 71 70 76 83 96 52 33 66  6 50 | 16 82  5 21 55 80 51 52 72 65  1 86 15 11 54 57 77 70 59 18 48 12 78 67 25
Card 143: 89 67  6 13 59 12 81 61 57 25 | 27 37 13 70 68 52 82  2 74 50 92  5 85 78 93 95 34 91 87 36 55 39 32  8 48
Card 144: 69 50 46 63 88  9  7 20 49 79 |  5 91 95 71 86 32 66 76 56 33 96 15 42 22 34 27  6 67 43 19 36 23 63 20 75
Card 145: 69 23 76  4 13 41 50 78 17 60 | 16 57 68 43 34 11 18 66 72  7 82  5 19 91 61 36 70 15 87 59 65 21 67  2  8
Card 146: 27 79  9 28 56 36 48 31 20  6 | 78 94 48  1 97 12 99 19 74 47 30 98 14 70 44 23 35 42 73 60 17 29 89 58 95
Card 147: 46 80 82  8 50 77 28 85 38 41 | 27 42 57 31 45 76 67 53 13 94 68 90 89 16 11 35 51 92 10 66 63 52  6 83 65
Card 148: 80 44 24 98 26 78  4  1 55 88 | 53  8 55 79 86 16 77 93 88 58 23 44 64 73 11 83 24 29 26 74 13 40 21 62  9
Card 149: 81 29 26 20 92 62 50 49 69 74 | 10 26 69 96 27 74 44 70 32 31  8 95 25 90  3 89 35  1 40 20 49 29 58 59 80
Card 150: 32 43 16 36 73 18 22 30 63 38 | 38 91 18 45 67 22 96 32 71  5 95 93 28 69 33 34 14 72 36 11 35 83 43 70 30
Card 151: 65 61 49 29 51 72 96 71 37 94 | 33 42 51 94 62 91 29 96 61 35 92 37 30  8 24 77 72 58 23 64 65 73 49 46 71
Card 152: 32 35 90  5 81 84 76 63 41 52 | 11 76 29 77 81 80  4 18 16 88 90 98 41 35 43 84 28 52 63  1 65  5 72 32 56
Card 153: 13 34 18 11 77 61 94 88  7 90 | 46 25 17 93  5 43 72 28 69  1 14 55 66 63 53 62 26 68 13 37 70 78 65 34 16
Card 154: 74 84 32 51  5 93  4 13 87 83 | 85 62 75 36 10 43 68 47 90 79  6 66 26 67 34 60 65  1 25 81 98 91 16 28 82
Card 155: 60  7 42 76  1 18 29 93 19 83 | 49 97 62 78 15 99 71 94 25 41 28  4 51  6  3 80 87 81 75 12 26 89 91  2 17
Card 156: 95 57 27  1 97 33 50 38 22 64 | 38 65 67 27 85 57  3 97 60 21 34 79 20 89 86 22 13  8 64 50 11 39 41 12  2
Card 157: 59 52 71 70 92 48 42 17 75 79 | 86 75  5 68 16 55 72 70 94 60  6  1 79 31 42 61 59 38 52 97 92 53 81 67 17
Card 158: 31 58 68  7 24 18 30 32 19 92 | 57  2 92 33 60 84 76 51 79 31 42 99 81  3 88 17 47 67 48 13  6 28 20 23 56
Card 159: 13 42 26 92 53 33 44 45 19 90 | 59 95  2 51 25 81 17 30  3 71 36 22 58 90 33 52  8 92 37  6 11 19 45 96 88
Card 160: 94 76 70 63 43 53 59 19 20 64 |  5 68 35 74 79 19 62 40 33 11 63 69 60 24  1 85 96 55 91 70 10 12 71 50 42
Card 161: 34 29 98 99 81 52 96 77 57 39 | 78 96 67  3  5 20 85 10 58 79 45 62 46 92 15 97 88  2 57 40 81 74 69 61 32
Card 162: 38 24 86 51 80  1 16 83 58 34 | 77 58 45 18 80 39 31 23 11 13 46 28 65 62 60 33 20  6 10 99 37 35 40 91 64
Card 163: 14 97  5 33 34 96 50 47 55 74 |  6 66 77 79 37 45 39 82 90  9 50 38 14 31 19 13 29 15 89 30 17 88 12 44 53
Card 164: 56 31 76  6 69 27 65 74 39 49 |  4 89  2 75 20 12 53 73 14 40 86 24 82 11 88 90 57 22 35 54 30 64 15 32 41
Card 165: 62 75 48 65 43 85  8 80 45 91 | 84 74 86 98 57 38 69 78 28 22  7 19 83 60  3 55 23 34 94 13  2 58 90 11 39
Card 166: 17 21 56 71 10 84 50 83 25 61 | 39 83 68 27 43  4 15 10 21 25 54  7 17 29 14 28 56 64 24 58 33 62 44 22 48
Card 167: 24 89 68  2 90 36 25 82 38 59 | 28 24 83 43 46  7 56  2 38 89  6 61 59 31 50 68 32 25 36  9 88 19 82 90 14
Card 168: 58 22 65 47 99 85 72 29 25 12 | 11 21 39 51 26 77  2 31 99 33 15 95  4 62 69 22 38 50 97 20 55 72  8 12 89
Card 169: 99 18 97  9 10 76 72 75 26 87 | 44 94 63 21 54 96 19  8 50  9 86 16 49 41 60  5 57  7 38 27 95 12 40 85  1
Card 170: 43 35 76 13 27 60 70 54 23 83 | 46 56 59 54 62 70 76 29 23 83 13 27 68 15 11  7 60  4 28 43 61 33 35 47 99
Card 171: 27 58 57 48 76 97  1 86 25 40 | 36 32 61 74 82 31 38 79 33 34 46  2 27 89 50 10 22 55 72 91 39 64 43 98 42
Card 172: 12 13 84 55 27 67 10 78 11 16 | 24  9 11 96 12 60 46  6 76 31 85 49 53  8 64 74 65 15 18 90 82 67 16 57 73
Card 173: 60 84 36 23 82 27 14 54 74  9 |  9 37 31 62 91 14 74 13 39 38 23 87  1 84 80 92 30 54 32 60 36 48 61 82 27
Card 174: 25 21 34 45 32 86 99 42 72 98 | 95 34 91 32 25 86 98 21 80 75 84 70  7 99 72 45 17 40 79 63  1 19 61 42 87
Card 175: 83 24 18 84 45 38 23 42 56 14 | 14 76 98 92 46 44 97 20 13 64 72 96 16 68 57 21  6 34  3 19 55 89  9 83  1
Card 176: 25 71 31 38  3 55 96 76  6 69 | 63 66 19 98 27 87 96  8 54 31 67 46 53 33 28 12 99 88 80 17 13 71 93 14  1
Card 177: 38 25 67 43 18  3 16 72 57 51 | 79 52 12 72 23 56 77 80 31 42 18 99 83 60 24 33 64 32 75 85  9 90 43  8  1
Card 178: 39 62 57  1 11 79  8 99 56 52 | 20 81 94 41 95  1 39 82  5 97  7 68 24 64 99 98 67 53  9 86 33 43 17 46 88
Card 179: 19 63 34 49 71 38 94 17  1 33 | 86 35 94 70 38 10 33 99 54  2 39 11 92 91 34 43 67 18 12 15 95  1 23 20 49
Card 180: 45 81 55 44 80 73  7 25 31 59 | 83 93 49 20 72 29 92 35 91 89 52 70 27 75 48 33 21 41 46 74 56  4  6 87 36
Card 181: 42 34 76 85 33 27 66 79 58 73 | 80 71 26  6 41 39 68 36 15 19 13 33 34 62 82 88 10  3 76 46 51 99 78 85 72
Card 182: 68 80 84 58 75 67 44 92 18 65 | 34 89  9 87 40 88 72 73 33 74 11  6 69  4 63 70 86  2  7 82 66 81 24 77 22
Card 183: 60 22  7 19 93 32 31 23 36 41 |  6 35 77 49 29 45 39 21 57 61 22 15 70 48 94 53 31 18 87 99 52  3 62 67 33
Card 184: 95 26 39 98 51 33 67 43 59 11 | 19 44 30 10 18 47 57 95 25 78 53 61  2 87 88 22 37 45 75 83 29 34 48 97 84
Card 185:  7 16 46 63 13  2 99  9 93 26 | 37 28 50 41 55 75 73  6 96 82 17 92 87 10 49 72 15 86 64 36 95 32 13  5 53
Card 186: 14 21 68  8 64 78 15 89 19 59 | 43 22 10 85 63 60 90 62 97 17 33 39  7  6 58 51 47 54 11 50 36  2 31 46 34"""


# text = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

lines = text.splitlines()
card_copies = defaultdict(lambda: 1)
for line in lines:
    game_name, winning_numbers, our_numbers = re.split(":|\|", line)
    game_id = int(game_name.split()[-1])

    winning_numbers = winning_numbers.strip().split()
    our_numbers = our_numbers.strip().split()

    commons_numbers = set(winning_numbers).intersection(set(our_numbers))

    card_copies[game_id] -= 0
    for _ in range(card_copies[game_id]):
        for i in range(game_id + 1, game_id + len(commons_numbers) + 1):
            card_copies[i] += 1


print(sum(list(card_copies.values())))
