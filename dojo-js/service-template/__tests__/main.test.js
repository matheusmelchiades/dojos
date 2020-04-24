const request = require('supertest')
const app = require('../src/app')

describe('Main', () => {

  it('It should return success', async () => {
    const response = await request(app).get('/')

    expect(response.status).toBe(200)
    expect(response.body).toEqual({ status: 'running' })
  })

  it('It should report error', async () => {
    const response = await request(app).get('/ROUTE_INVALID')

    expect(response.status).toBe(404)
  })
})
