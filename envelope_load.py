def conductive_gain_w(u_value, area_m2, cltd_k):
    """Calculate opaque wall or roof conductive heat gain (W) using Q = U * A * CLTD."""
    if u_value <= 0 or area_m2 <= 0:
        raise ValueError("U-value and surface area must be greater than zero.")
    if cltd_k < 0:
        raise ValueError("Cooling Load Temperature Difference (CLTD) cannot be negative.")
    return round(u_value * area_m2 * cltd_k, 2)


def solar_glazing_gain_w(area_m2, shgc, irradiance_w_m2, shading_factor=1.0):
    """Calculate transmitted solar heat gain through glazing (W)."""
    if area_m2 <= 0 or irradiance_w_m2 < 0:
        raise ValueError("Glazing area must be positive and irradiance non-negative.")
    if not (0 < shgc <= 1.0) or not (0 < shading_factor <= 1.0):
        raise ValueError("SHGC and shading factor must be within (0, 1.0].")
    return round(area_m2 * shgc * irradiance_w_m2 * shading_factor, 2)


def total_envelope_load_kw(wall_w, roof_w, glazing_cond_w, glazing_solar_w):
    """Aggregate envelope heat gain components and return total cooling load in kW."""
    total_w = wall_w + roof_w + glazing_cond_w + glazing_solar_w
    return round(total_w / 1000.0, 3)


if __name__ == "__main__":
    wall_gain = conductive_gain_w(u_value=0.45, area_m2=40.0, cltd_k=14.0)
    roof_gain = conductive_gain_w(u_value=0.25, area_m2=100.0, cltd_k=22.0)
    glass_cond = conductive_gain_w(u_value=2.80, area_m2=15.0, cltd_k=8.0)
    glass_solar = solar_glazing_gain_w(area_m2=15.0, shgc=0.35, irradiance_w_m2=650.0)
    peak_kw = total_envelope_load_kw(wall_gain, roof_gain, glass_cond, glass_solar)

    print(
        f"Envelope Load Breakdown -> Wall: {wall_gain} W | Roof: {roof_gain} W | "
        f"Glazing (Cond + Solar): {glass_cond + glass_solar} W | Total Peak Load: {peak_kw} kW"
    )