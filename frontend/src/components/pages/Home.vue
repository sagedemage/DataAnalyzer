<script>
    export default (await import('vue')).defineComponent({
    data: () => ({
      data: null,
      group: null,
      shapes: [
            {id: 0, length: 10, width: 10, area: 10*10},
            {id: 1, length: 12, width: 12, area: 12*12},
            {id: 2, length: 14, width: 14, area: 14*14},
            {id: 3, length: 16, width: 16, area: 16*16},
            {id: 4, length: 18, width: 18, area: 18*18},
            {id: 5, length: 20, width: 20, area: 20*20},
            {id: 6, length: 22, width: 22, area: 22*22},
            {id: 7, length: 24, width: 24, area: 24*24},
            {id: 8, length: 26, width: 26, area: 26*26},
            {id: 9, length: 28, width: 28, area: 28*28},
        ]
    }),

    methods: {
	    async test() {
            /* Test request to the backend */
            const response = await fetch("http://localhost:8000/api/test");
            this.data = await response.json();
            console.log(this.data);
  	    }
	}
})
</script>

<template>
    <h1>Home</h1>
    <p>This is the home page</p>
    <v-btn color="blue" @click="test()">test</v-btn>
    <p>Data: {{ data }}</p>
</template>