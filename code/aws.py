# Definición de los parámetros
tarifas_por_hora = [0.154, 0.616, 1.6832]  # Tarifas por hora de cada máquina
memoria_ram = [16, 64, 128]  # En GiB
almacenamiento_ssd = [40, 256, 512]  # En GB
data_out = [1000, 3000, 10000]  # En GB, total de Data Out por mes

# Costo de EBS por GB al mes
costo_ebs_por_gb = 0.08

# Costo de transferencia de datos
costo_trans_prim_10tb = 0.09  # Costo por GB
costo_trans_40tb_siguientes = 0.085  # Costo por GB
costo_trans_100tb_siguientes = 0.07  # Costo por GB
costo_trans_mas_150tb = 0.05  # Costo por GB

# Horas al mes para el cálculo del costo mensual
horas_mes = 730

# Costos mensuales
costos_totales = []

# Cálculo de costos
for i in range(3):
    costo_horas = tarifas_por_hora[i] * horas_mes
    costo_ebs = almacenamiento_ssd[i] * costo_ebs_por_gb
    gb_salientes = data_out[i] - 100  # primeros 100 GB son gratis
    
    if gb_salientes <= 10240:  # Dentro de los primeros 10 TB
        costo_data_out = gb_salientes * costo_trans_prim_10tb
    elif gb_salientes <= 51200:  # Siguiente 40 TB
        costo_data_out = (10240 * costo_trans_prim_10tb) + \
                         ((gb_salientes - 10240) * costo_trans_40tb_siguientes)
    elif gb_salientes <= 153600:  # Siguiente 100 TB
        costo_data_out = (10240 * costo_trans_prim_10tb) + \
                         (40960 * costo_trans_40tb_siguientes) + \
                         ((gb_salientes - 51200) * costo_trans_100tb_siguientes)
    else:  # Más de 150 TB
        costo_data_out = (10240 * costo_trans_prim_10tb) + \
                         (40960 * costo_trans_40tb_siguientes) + \
                         (102400 * costo_trans_100tb_siguientes) + \
                         ((gb_salientes - 153600) * costo_trans_mas_150tb)
    
    costo_total = costo_horas + costo_ebs + costo_data_out
    costos_totales.append(costo_total)

print(costos_totales)
