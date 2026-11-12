class EstadoInvalidoError(Exception):
    pass


class TicketTecnico:
    ESTADOS = ("Abierto", "En Proceso", "Cerrado")
    PRIORIDADES = ("Baja", "Media", "Alta")
    TRANSICIONES = {
        "Abierto": ("En Proceso", "Cerrado"),
        "En Proceso": ("Abierto", "Cerrado"),
        "Cerrado": ("Abierto",),
    }
    SLA_BASE = {"Alta": 4, "Media": 24, "Baja": 72}

    def __init__(self, id_ticket, titulo, prioridad):
        if prioridad not in self.PRIORIDADES:
            raise ValueError(f"Prioridad no valida: {prioridad}")
        self._id = id_ticket
        self._titulo = titulo
        self._estado = "Abierto"
        self._prioridad = prioridad

    @property
    def id(self):
        return self._id

    @property
    def titulo(self):
        return self._titulo

    @property
    def estado(self):
        return self._estado

    @property
    def prioridad(self):
        return self._prioridad

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado not in self.ESTADOS:
            raise EstadoInvalidoError(f"El estado '{nuevo_estado}' no existe")
        if nuevo_estado not in self.TRANSICIONES[self._estado]:
            raise EstadoInvalidoError(
                f"No se puede pasar de '{self._estado}' a '{nuevo_estado}'"
            )
        self._estado = nuevo_estado

    def iniciar(self):
        self.cambiar_estado("En Proceso")

    def cerrar(self):
        self.cambiar_estado("Cerrado")

    def reabrir(self):
        self.cambiar_estado("Abierto")

    def calcular_sla(self):
        return self.SLA_BASE[self._prioridad]

    def __str__(self):
        return (
            f"{type(self).__name__} #{self._id}: {self._titulo} | "
            f"{self._estado} | Prioridad {self._prioridad}"
        )


class TicketHardware(TicketTecnico):
    def __init__(self, id_ticket, titulo, prioridad, componente):
        super().__init__(id_ticket, titulo, prioridad)
        self.componente = componente

    def calcular_sla(self):
        return super().calcular_sla() * 2


class TicketSoftware(TicketTecnico):
    def __init__(self, id_ticket, titulo, prioridad, sistema_operativo):
        super().__init__(id_ticket, titulo, prioridad)
        self.sistema_operativo = sistema_operativo

    def calcular_sla(self):
        return super().calcular_sla() // 2


if __name__ == "__main__":
    ticket_hw = TicketHardware(1, "Pantalla rota", "Alta", "Monitor")
    ticket_sw = TicketSoftware(2, "Excel no abre", "Media", "Windows 11")

    print("--- Polimorfismo: calcular_sla() ---")
    for ticket in (ticket_hw, ticket_sw):
        print(ticket)
        print("SLA:", ticket.calcular_sla(), "horas")

    print("--- Transiciones validas ---")
    ticket_hw.iniciar()
    print(ticket_hw.estado)
    ticket_hw.cerrar()
    print(ticket_hw.estado)

    print("--- Transicion invalida ---")
    try:
        ticket_hw.cambiar_estado("En Proceso")
    except EstadoInvalidoError as error:
        print("Error controlado:", error)

    print("--- Estado inexistente ---")
    try:
        ticket_sw.cambiar_estado("Pendiente")
    except EstadoInvalidoError as error:
        print("Error controlado:", error)

    print("--- Prioridad invalida ---")
    try:
        TicketSoftware(3, "Prueba", "Urgente", "Linux")
    except ValueError as error:
        print("Error controlado:", error)