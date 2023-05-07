<script>
    export default {
    data: () => ({
      drawer: false,
      group: null,
      shapes: [
        {id: 0, length: 10, width: 10, area: 10*10},
        {id: 1, length: 12, width: 12, area: 12*12},
        {id: 2, length: 14, width: 14, area: 14*14},
        {id: 3, length: 16, width: 16, area: 16*16},
        {id: 4, length: 18, width: 18, area: 18*18},
        ]
    }),
}
</script>


<template>
    <h1>Dashboard</h1>
    <p>This is the dashboard page</p>
    <table>
        <tr>
            <th>Length</th>
            <th>Width</th>
            <th>Area</th>
        </tr>
        <tr v-for="shape in shapes" :key="shape.id">
            <td>{{ shape.length }}</td>
            <td>{{ shape.width }}</td>
            <td>{{ shape.area }}</td>
        </tr>
    </table>
</template>

<style scoped>
    table {
        border:0.5px solid black;
        text-align: center;
    }

    th, td {
        border: 1px solid black;
        padding-left: 10px;
        padding-right: 10px;
    }
</style>