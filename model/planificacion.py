# -*- coding: utf-8 -*-#

from openerp import models, fields, api


class PlanificacionNivel(models.Model):
    _name = 'planificacion.nivel'

    name = fields.Char(string="Descripción")
    institucion_id = fields.Many2one('res.company', string="Institucion")
    active = fields.Boolean('Activo?', default=False)


class PlanificacionTipo(models.Model):
    _name = 'planificacion.tipo'

    name = fields.Char(string="Descripción")
    institucion_id = fields.Many2one('res.company', string="Institucion")
    active = fields.Boolean('Activo?', default=False)


class PlanificacionUnidades(models.Model):
    _name = 'planificacion.unidades'

    name = fields.Char(string="Descripción")
    institucion_id = fields.Many2one('res.company', string="Institucion")
    active = fields.Boolean('Activo?', default=False)
    
    
class PlanificacionAsignaturas(models.Model):
    _name = 'planificacion.asignaturas'

    name = fields.Char(string="Descripción")
    institucion_id = fields.Many2one('res.company', string="Institucion")
    active = fields.Boolean('Activo?', default=False)
    nivel_id = fields.Many2one('planificacion.nivel', string="Nivel")
    horas = fields.Float(string="Horas")
    

class PlanificacionEjes(models.Model):
    _name = 'planificacion.ejes'

    name = fields.Char(string="Descripción")
    institucion_id = fields.Many2one('res.company', string="Institucion")
    active = fields.Boolean('Activo?', default=False)
    nivel_id = fields.Many2one('planificacion.nivel', string="Nivel")
    asignatura_id = fields.Many2one('planificacion.asignaturas', string="Asignaturas")
    
    
class PlanificacionCurriculo(models.Model):
    _name = 'planificacion.curriculo'

    name = fields.Char(string="Descripción")
    institucion_id = fields.Many2one('res.company', string="Institucion")
    active = fields.Boolean('Activo?', default=False)
    nivel_id = fields.Many2one('planificacion.nivel', string="Nivel")
    asignatura_id = fields.Many2one('planificacion.asignaturas', string="Asignaturas")
    eje_id = fields.Many2one('planificacion.ejes', string="Eje")
    tipo_id = fields.Many2one('planificacion.tipo', string="Tipo")
    unidad_id = fields.Many2one('planificacion.unidades', string="Unidad")
    

class PlanificacionIndicadores(models.Model):
    _name = 'planificacion.indicadores'

    name = fields.Char(string="Descripción")
    institucion_id = fields.Many2one('res.company', string="Institucion")
    active = fields.Boolean('Activo?', default=False)
    eje_id = fields.Many2one('planificacion.ejes', string="Eje")
    unidad_id = fields.Many2one('planificacion.unidades', string="Unidad")
    curriculo_id = fields.Many2one('planificacion.curriculo', string="Curriculo")
    
    
class PlanificacionClases(models.Model):
    _name = 'planificacion.clases'

    name = fields.Char(string="Descripción")
    fecha = fields.Date(string="Fecha")
    institucion_id = fields.Many2one('res.company', string="Institucion")
    active = fields.Boolean('Activo?', default=False)
    nivel_id = fields.Many2one('planificacion.nivel', string="Nivel")
    asignatura_id = fields.Many2one('planificacion.asignaturas', string="Asignatura")
    objetivo = fields.Text(string="Objetivo")
    clases_lines = fields.One2many('planificacion.clases.lines', 'clases_id', string="Lineas de clases")


class PlanificacionClasesLines(models.Model):
    _name = 'planificacion.clases.lines'

    clases_id = fields.Many2one('planificacion.clases', string="Clases")
    curriculo_id = fields.Many2one('planificacion.curriculo', string="Curriculo")