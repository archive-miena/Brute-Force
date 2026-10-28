from itertools import permutations

# Waktu tempuh tiap jalur (menit)
waktu = {
    ("A", "B"): 9,  ("A", "C"): 14, ("A", "D"): 6,  ("A", "E"): 17, ("A", "F"): 11,
    ("B", "C"): 8,  ("B", "D"): 15, ("B", "E"): 5,  ("B", "F"): 13,
    ("C", "D"): 4,  ("C", "E"): 12, ("C", "F"): 7,
    ("D", "E"): 10, ("D", "F"): 18,
    ("E", "F"): 3,
}


def jarak(a, b):
    return waktu.get((a, b)) or waktu[(b, a)]


def brute_force(start="A", simpul=("B", "C", "D", "E", "F")):
    semua = []
    for p in permutations(simpul):          # 5! = 120 susunan
        if p[0] > p[-1]:                    # buang rute kebalikan -> 60 rute unik
            continue
        rute = [start, *p, start]
        langkah = [jarak(rute[i], rute[i + 1]) for i in range(len(rute) - 1)]
        semua.append((rute, langkah, sum(langkah)))
    return semua


if __name__ == "__main__":
    hasil = brute_force()

    print(f"{'No':<4}{'Rute':<22}{'Perhitungan':<28}Total")
    for no, (rute, langkah, total) in enumerate(hasil, 1):
        print(f"{no:<4}{' - '.join(rute):<22}{' + '.join(map(str, langkah)):<28}{total}")

    urut = sorted(hasil, key=lambda x: x[2])

    print("\n5 rute tercepat:")
    for i, (rute, _, total) in enumerate(urut[:5], 1):
        print(f"{i}. {' - '.join(rute)}  = {total} menit")

    terbaik, langkah, total = urut[0]
    print("\nRute tercepat :", " -> ".join(terbaik))
    print("Perhitungan   :", " + ".join(map(str, langkah)), "=", total, "menit")
    print("Rute terlama  :", " -> ".join(urut[-1][0]), "=", urut[-1][2], "menit")
    print("Jumlah rute   :", len(hasil))