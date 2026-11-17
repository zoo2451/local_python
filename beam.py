# Simply supported beam with a uniform load
w = float(input("Uniform load w (kip/ft): "))
L = float(input("Span L (ft): "))
E = 29000      # ksi, steel
I = 510        # in^4, W18x35

M_max = w * L**2 / 8                                  # kip-ft
delta = 5 * (w / 12) * (L * 12)**4 / (384 * E * I)    # in

print(f"Maximum moment: {M_max:.1f} kip-ft")
print(f"Maximum deflection: {delta:.2f} in")
print(f"L/360 limit: {L * 12 / 360:.2f} in")

if delta <= L * 12 / 360:
    print("Deflection OK")
else:
    print("Deflection too large - choose a stiffer beam")