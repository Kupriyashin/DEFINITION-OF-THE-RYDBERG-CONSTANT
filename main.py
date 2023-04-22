import numpy
from loguru import logger


# ФУНКЦИЯ ДЛЯ РАСЧЕТА ПОСТОЯННОЙ РИТБЕРГА, КОТОРАЯ ПРИНИМАЕТ ДЛИНУ ВОЛНЫ И НОМЕР УРОВНЯ
def const_Ritberg(wavelength: numpy.float64, number_level: int) -> numpy.float64:
    ritberg_const = numpy.divide(
        1,
        numpy.dot(
            wavelength,
            numpy.divide(
                1,
                2 ** 2
            ) - numpy.divide(
                1,
                number_level ** 2
            )
        )
    )
    return ritberg_const


def rascheti():
    # ВХОДНЫЕ ПАРАМЕТРЫ
    wavelength_3_2 = numpy.dot(632, 10 ** (-9))
    wavelength_4_2 = numpy.dot(481, 10 ** (-9))
    wavelength_5_2 = numpy.dot(463, 10 ** (-9))

    logger.info(f"\nДлина волны при переходе с 3 на 2 уровень: {wavelength_3_2}\n"
                f"Длина волны при переходе с 4 на 2 уровень: {wavelength_4_2}\n"
                f"Длина волны при переходе с 5 на 2 уровень: {wavelength_5_2}\n")

    # РАСЧЕТ ПОСТОЯННЫХ РИТБЕРГА ДЛЯ ДЛИН ВОЛН
    ritberg_wavelength_3_2 = numpy.dot(const_Ritberg(wavelength=wavelength_3_2, number_level=3), 10 ** (-7))

    ritberg_wavelength_4_2 = numpy.dot(const_Ritberg(wavelength=wavelength_4_2, number_level=4), 10 ** (-7))
    ritberg_wavelength_5_2 = numpy.dot(const_Ritberg(wavelength=wavelength_5_2, number_level=5), 10 ** (-7))

    logger.info(f"\nПостоянная ритберга для длины волны {wavelength_3_2} составляет {ritberg_wavelength_3_2}e+07\n"
                f"Постоянная ритберга для длины волны {wavelength_4_2} составляет {ritberg_wavelength_4_2}e+07\n"
                f"Постоянная ритберга для длины волны {wavelength_5_2} составляет {ritberg_wavelength_5_2}e+07\n")

    # СРЕДНЕЕ ЗНАЧЕНИЕ ПОСТОЯННОЙ РИТБЕРГА
    sred_ritberg_const = numpy.mean([ritberg_wavelength_3_2, ritberg_wavelength_4_2, ritberg_wavelength_5_2])
    logger.info(f"\nСреднее значение постоянной Ритберга составляет: {sred_ritberg_const}e+07")

    # СРЕДНЕКВАДРАТИЧЕСКАЯ ОБСОЛЮТНАЯ ПОГРЕШНОСТЬ
    abs_3_2 = numpy.abs(sred_ritberg_const - ritberg_wavelength_3_2)
    abs_4_2 = numpy.abs(sred_ritberg_const - ritberg_wavelength_4_2)
    abs_5_2 = numpy.abs(sred_ritberg_const - ritberg_wavelength_5_2)
    sred_abs_error = numpy.mean([abs_3_2, abs_4_2, abs_5_2])

    logger.info(f"\nСреднеквадратическая абсолютная погрешность: {sred_abs_error}e+07")

    # ПРОВЕРКА РЕЗУЛЬТАТА
    ritberg_teor = numpy.dot(1.0974, 1)

    otnos_raznost = numpy.dot(
        numpy.divide(
            ritberg_teor - sred_ritberg_const,
            ritberg_teor
        ),
        100
    )

    logger.info(f"\nТеоретическое значение постоянной Ритберга: {ritberg_teor}e+07\n"
                f"Вычесленное занчение: {sred_ritberg_const}e+07\n"
                f"Относительная разность составляет: {otnos_raznost} %")


if __name__ == '__main__':
    rascheti()
