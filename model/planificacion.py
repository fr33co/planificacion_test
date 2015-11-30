# -*- coding: utf-8 -*-#

from openerp import models, fields, api
from openerp.tools.translate import _


class PlanificacionNivel(models.Model):
    _name = 'planificacion.nivel'
    _order = 'name'

    name = fields.Char(string="Descripción")
    institucion_id = fields.Many2one('res.company', string="Institucion")
    active = fields.Boolean('Activo?', default=False)


class PlanificacionTipo(models.Model):
    _name = 'planificacion.tipo'
    _order = 'name'

    name = fields.Char(string="Descripción")
    institucion_id = fields.Many2one('res.company', string="Institucion")
    active = fields.Boolean('Activo?', default=False)


class PlanificacionUnidades(models.Model):
    _name = 'planificacion.unidades'
    _order = 'name'

    name = fields.Char(string="Descripción")
    institucion_id = fields.Many2one('res.company', string="Institucion")
    active = fields.Boolean('Activo?', default=False)
    
    
class PlanificacionAsignaturas(models.Model):
    _name = 'planificacion.asignaturas'
    _order = 'name'

    name = fields.Char(string="Descripción")
    institucion_id = fields.Many2one('res.company', string="Institucion")
    active = fields.Boolean('Activo?', default=False)
    nivel_id = fields.Many2one('planificacion.nivel', string="Nivel")
    horas = fields.Float(string="Horas")
    

class PlanificacionEjes(models.Model):
    _name = 'planificacion.ejes'
    _order = 'name'

    name = fields.Char(string="Descripción")
    institucion_id = fields.Many2one('res.company', string="Institucion")
    active = fields.Boolean('Activo?', default=False)
    nivel_id = fields.Many2one('planificacion.nivel', string="Nivel")
    asignatura_id = fields.Many2one('planificacion.asignaturas', string="Asignaturas")
    
    
class PlanificacionCurriculo(models.Model):
    _name = 'planificacion.curriculo'
    _order = 'name'
        

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
    _order = 'name'

    name = fields.Char(string="Descripción")
    institucion_id = fields.Many2one('res.company', string="Institucion")
    active = fields.Boolean('Activo?', default=False)
    eje_id = fields.Many2one('planificacion.ejes', string="Eje")
    unidad_id = fields.Many2one('planificacion.unidades', string="Unidad")
    curriculo_id = fields.Many2one('planificacion.curriculo', string="Curriculo")
    clases_lines_id = fields.Many2one('planificacion.clases.lines', string="Clases Lines")
    
class PlanificacionClases(models.Model):
    _name = 'planificacion.clases'
    _order = 'name'

    name = fields.Char(string="Descripción")
    fecha = fields.Date(string="Fecha")
    institucion_id = fields.Many2one('res.company', string="Institucion")
    active = fields.Boolean('Activo?', default=False)
    nivel_id = fields.Many2one('planificacion.nivel', string="Nivel")
    asignatura_id = fields.Many2one('planificacion.asignaturas', string="Asignatura")
    objetivo = fields.Text(string="Objetivo")
    planificacion_clases_lines = fields.One2many('planificacion.clases.lines', 'clases_id', string="Lineas de clases")
    adjunto = fields.One2many('ir.attachment',compute='_get_adjuntos')


    def _get_adjuntos(self):
        for rec in self:
            attachments = self.env['ir.attachment'].search([('res_model','=','planificacion.clases'),('res_id','=',rec.id)])
            self.adjunto = attachments

    def attachment_tree_view(self, cr, uid, ids, context):
        domain = [
             '&', ('res_model', '=', 'planificacion.clases'), ('res_id', 'in', ids),
        ]
        res_id = ids and ids[0] or False
        return {
            'name': _('Documents'),
            'domain': domain,
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'tree,form',
            'view_type': 'form',
            'limit': 80,
            'context': "{'default_res_model': '%s','default_res_id': %d}" % (self._name, res_id)
        }

class PlanificacionClasesLines(models.Model):
    _name = 'planificacion.clases.lines'

    clases_id = fields.Many2one('planificacion.clases', string="Clases")
    curriculo_id = fields.Many2one('planificacion.curriculo', string="Curriculo")
    indicadores_ids = fields.One2many('planificacion.indicadores', 'clases_lines_id', string="Indicadores")