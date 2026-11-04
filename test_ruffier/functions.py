def ruffier_index(pulse_1, pulse_2, pulse_3):
    return (4*(pulse_1, pulse_2, pulse_3) - 200)/10

## POR FAVOR LIMPIA ESTA MIERDA QUE SE VE HORRIBLE Y PONLE UNA ESTRUCTURA DE CASOS DIOS MIO???
## como se factoriza un codigo.

def ruffier_results(ruffier, age):
    if age >= 15:
        if ruffier >= 6 and ruffier <= 10.9:
            results = "Indice promedio"
        elif ruffier >= 11 and ruffier <= 14.9:
            results = "Indice satisfactorio"
        elif  ruffier >= 0.5 and ruffier <= 5.9:
            results = "Indice mayor al promedio"
        elif ruffier <= 0.4:
            results = "Indice alto"
        elif ruffier >= 15:
            results = "Indice bajo"
    elif age >= 13 and age <= 14:
        if ruffier >= 7.5 and ruffier <= 12.4:
            results = "Indice promedio"
        elif ruffier >= 12.5 and ruffier <= 16.4:
            results = "Indice satisfactorio"
        elif  ruffier >= 2 and ruffier <= 7.4:
            results = "Indice mayor al promedio"
        elif ruffier <= 1.9:
            results = "Indice alto"
        elif ruffier >= 16.5:
            results = "Indice bajo"
    elif age >= 11 and age <= 12:
        if ruffier >= 9 and ruffier <= 13.9:
            results = "Indice promedio"
        elif ruffier >= 14 and ruffier <= 17.9:
            results = "Indice satisfactorio"
        elif  ruffier >= 3.5 and ruffier <= 8.9:
            results = "Indice mayor al promedio"
        elif ruffier <= 3.4:
            results = "Indice alto"
        elif ruffier >= 18:
            results = "Indice bajo"
    elif age >= 9 and age <= 10:
        if ruffier >= 10.5 and ruffier <= 15.4:
            results = "Indice promedio"
        elif ruffier >= 15.5 and ruffier <= 19.4:
            results = "Indice satisfactorio"
        elif  ruffier >= 5 and ruffier <= 10.4:
            results = "Indice mayor al promedio"
        elif ruffier <= 4.9:
            results = "Indice alto"
        elif ruffier >= 19.5:
            results = "Indice bajo"
    elif age >= 7 and age <= 9:
        if ruffier >= 12 and ruffier <= 16.9:
            results = "Indice promedio"
        elif ruffier >= 17 and ruffier <= 20.9:
            results = "Indice satisfactorio"
        elif  ruffier >= 6.5 and ruffier <= 11.9:
            results = "Indice mayor al promedio"
        elif ruffier <= 6.4:
            results = "Indice alto"
        elif ruffier >= 21:
            results = "Indice bajo"

    return results